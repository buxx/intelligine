FROM ubuntu:14.04

# Disable frontend for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# All deb required packages
RUN apt-get update
RUN apt-get install -y git python3-pip mercurial python3-dev python3-numpy libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev

# Build pygame (curent default graphic viewer)
RUN cd / && hg clone https://bitbucket.org/pygame/pygame
RUN cd /pygame && python3 setup.py build
RUN cd /pygame && sudo python3 setup.py install

# Install intelligine and it's dependencies
RUN cd / && git clone https://github.com/buxx/intelligine.git
RUN pip3 install -r /intelligine/requirements.txt
