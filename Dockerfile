FROM ubuntu:18.04

MAINTAINER EDGAR PEREZ SAMPEDRO <edgar.perez.sampedro@gmail.com>

RUN apt-get update

# ANACONDA3
RUN apt-get update && \
    apt-get install git-core -y && \
    apt-get install -y curl build-essential && \
    apt-get clean && \
    rm -rf /var/tmp /tmp /var/lib/apt/lists/*

ENV CONDA_DIR="/conda" 
ENV PATH="$CONDA_DIR/bin:$PATH"
RUN curl -sSL -o installer.sh https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh && \
    bash /installer.sh -b -f && \
    rm /installer.sh

ENV PATH "$PATH:/root/anaconda3/bin"

COPY requirements.txt requirements.txt

RUN ["/bin/bash", "-c", "pip install -r requirements.txt"]

RUN mkdir /root/politician_bot_course \
    && cd /root/politician_bot_course 
 
#Set working directory
WORKDIR /root/politician_bot_course
EXPOSE 5555

CMD ["/bin/bash", "-c", "git clone https://github.com/Fidu/politician_bot_course.git /root/politician_bot_course; /bin/bash"]


