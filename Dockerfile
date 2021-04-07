FROM python:3.9

RUN apt-get update \
 && apt-get install -y \
  apt-utils \
  glances \
  sshfs \
  cifs-utils \
  sudo \
  locales \
  git \
  vim-tiny \
  less \
  curl \
  python3-dev \
  graphviz \
  libgraphviz-dev \ 
  pkg-config \
  gpg \
  wget \
  rubygems

WORKDIR /usr/src/app
# package dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app .