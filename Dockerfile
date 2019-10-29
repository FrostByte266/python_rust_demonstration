FROM python:3.8.0-buster

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y --default-toolchain nightly
RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc

COPY requirements.txt /requirements.txt 
RUN pip install -r requirements.txt

COPY . .
