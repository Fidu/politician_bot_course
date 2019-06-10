import torch
from torch import nn
import torch.nn.functional as F

import numpy as np


class GeneratorTextLSTM(nn.Module):
    def __init__(self, data_input, n_hidden=256, n_layers=2,
                 drop_prob=0.5, lr=0.001):
        super().__init__()
        self.drop_prob = drop_prob
        self.n_layers = n_layers
        self.n_hidden = n_hidden
        self.lr = lr

        # loading character dictionaries
        self.chars = data_input['chars']
        self.int2char = data_input['int2char']
        self.char2int = data_input['char2int']

        # define the LSTM
        self.lstm = nn.LSTM(len(self.chars), n_hidden, n_layers,
                            dropout=drop_prob, batch_first=True)

        # define a dropout layer
        self.dropout = nn.Dropout(drop_prob)

        # define the final, fully-connected output layer
        self.fc = nn.Linear(n_hidden, len(self.chars))

    def forward(self, x, hidden):
        """ Forward pass through the network.
            These inputs are x, and the hidden/cell state `hidden`. """

        # Get the outputs and the new hidden state from the lstm
        r_output, hidden = self.lstm(x, hidden)

        # pass through a dropout layer
        out = self.dropout(r_output)

        # Stack up LSTM outputs using view
        # you may need to use contiguous to reshape the output
        out = out.contiguous().view(-1, self.n_hidden)

        # put x through the fully-connected layer
        out = self.fc(out)

        # return the final output and the hidden state
        return out, hidden

    def init_hidden(self, batch_size, device='cpu'):
        """ Initializes hidden state """
        # Create two new tensors with sizes n_layers x batch_size x n_hidden,
        # initialized to zero, for hidden state and cell state of LSTM
        weight = next(self.parameters()).data

        hidden = (weight.new(self.n_layers, batch_size, self.n_hidden).zero_().to(device),
                  weight.new(self.n_layers, batch_size, self.n_hidden).zero_().to(device))

        return hidden


def one_hot_encode(array_text, n_labels):
    """Function to load data to train the model

       Args:
           array_text (np.array): np.array with text converted in numbers
           n_labels (int): number of distinct chars in the text
       Returns:
           one_hot (np.array): data from array_text into values 0 to 1
    """
    # Initialize the the encoded array
    one_hot = np.zeros((np.multiply(*array_text.shape), n_labels), dtype=np.float32)

    # Fill the appropriate elements with ones
    one_hot[np.arange(one_hot.shape[0]), array_text.flatten()] = 1.

    # Finally reshape it to get back to the original array
    one_hot = one_hot.reshape((*array_text.shape, n_labels))

    return one_hot


def predict(model, char, h=None, top_k=None, device='cpu'):
    """ Given a character, predict the next character.
        Returns the predicted character and the hidden state.
    """
    # tensor inputs
    x = np.array([[model.char2int[char]]])
    x = one_hot_encode(x, len(model.chars))
    inputs = torch.from_numpy(x).to(device)

    # detach hidden state from history
    h = tuple([each.data for each in h])
    # get the output of the model
    out, h = model(inputs, h)

    # get the character probabilities
    p = F.softmax(out, dim=1).data.cpu()

    # get top characters
    if top_k is None:
        top_ch = np.arange(len(model.chars))
    else:
        p, top_ch = p.topk(top_k)
        top_ch = top_ch.numpy().squeeze()

    # select the likely next character with some element of randomness
    p = p.numpy().squeeze()
    char = np.random.choice(top_ch, p=p / p.sum())

    # return the encoded value of the predicted char and the hidden state
    return model.int2char[str(char)], h


def sample(model, size, prime='hola', top_k=None, device='cpu'):
    model.to(device)
    model.eval()  # eval mode

    # First off, run through the prime characters
    chars = [ch for ch in prime]
    h = model.init_hidden(1)
    for ch in prime:
        char, h = predict(model, ch, h, top_k=top_k)

    chars.append(char)

    # Now pass in the previous character and get a new one
    for ii in range(size):
        char, h = predict(model, chars[-1], h, top_k=top_k)
        chars.append(char)

    return ''.join(chars)


def load_model(data_input, path_model):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = GeneratorTextLSTM(data_input, 512, 2)
    model.load_state_dict(
        torch.load(path_model, map_location={'cuda:0': 'cpu'}))  # Choose whatever GPU device number you want
    model.to(device)
    return model

