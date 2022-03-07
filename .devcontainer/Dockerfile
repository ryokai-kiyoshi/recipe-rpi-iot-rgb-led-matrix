# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.217.4/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use hirsuite or bionic on local arm64/Apple Silicon): hirsute, focal, bionic

FROM ubuntu:20.04

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>


# RUN sudo sed -i -E 's/(^Defaults\s+secure_path=\")/\1\/usr\/local\/python\/bin:/' /etc/sudoers && \
RUN dpkg --add-architecture armhf && \
    apt update && \
    apt --yes install wget wiringpi libc6-armhf sudo && \
    wget https://project-downloads.drogon.net/wiringpi-latest.deb && \
    dpkg -i wiringpi-latest.deb && \
    useradd -m -d /home/devel -U -s /usr/bin/bash devel && \
    apt --yes install python3 python3-pip python-rpi.gpio && \
    pip install RPi.gpio && \
    echo "devel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers 