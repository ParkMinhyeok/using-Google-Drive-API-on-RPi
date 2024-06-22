#!/bin/bash

echo "Installing required packages..."
sudo apt-get update
sudo apt-get install -y build-essential cmake pkg-config
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libfontconfig1-dev libcairo2-dev
sudo apt-get install -y libgdk-pixbuf2.0-dev libpango1.0-dev
sudo apt-get install -y libgtk2.0-dev libgtk-3-dev
sudo apt-get install -y libatlas-base-dev gfortran
sudo apt-get install -y python3-dev

echo "Installing pip and numpy..."
sudo apt-get install -y python3-pip
pip3 install numpy

echo "Installing Google API client libraries..."
pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib

echo "Installing OpenCV..."
pip3 install opencv-python

echo "Verifying OpenCV installation..."
python3 - <<EOF
import cv2
print("OpenCV version:", cv2.__version__)
EOF

echo "Installation complete!"
