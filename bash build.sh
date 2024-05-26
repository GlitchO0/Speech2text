#!/bin/bash

# Install PortAudio dependencies
apt-get update
apt-get install -y portaudio19-dev

# Install Python dependencies
pip install -r requirements.txt
