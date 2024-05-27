#!/usr/bin/env bash
# install_dependencies.sh

set -e

# Update package list and install portaudio
apt-get update && apt-get install -y portaudio19-dev

# Install Python dependencies
pip install -r requirements.txt
