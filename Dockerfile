FROM python

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc

COPY requirements.txt /requirements.txt 
RUN pip install -r requirements.txt

COPY . .
