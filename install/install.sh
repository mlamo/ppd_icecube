#!/bin/bash


# paths and definitions
desktop_path=${HOME}/Bureau/
usb_path=/media/${USER}/C7D4-163E
echo 'export PATH=$PATH:~/.local/bin' > ~/.bashrc # do this be
source ~/.bashrc
#export PATH=$PATH:~/.local/bin

# Python packages
#python3 ${usb_path}/install/get-pip.py
#curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# curl is not installed by default, wth
wget https://bootstrap.pypa.io/get-pip.py 
python3 get-pip.py
pip install --user jupyter numpy healpy matplotlib pandas astropy
pip install --user --upgrade scipy
pip install --user jupyterlab-language-pack-fr-FR

# copy the PPD files and the launcher
cp -R ${usb_path}/ppd ${desktop_path}/ppd
cp ${usb_path}/install/ppd.sh ~/.local/bin/
chmod +x ~/.local/bin/ppd.sh
# can execute it from command line or context menu
# but warn them not to run it twice (TODO check does Jupyter 7 prevent double launches?)
cp ${usb_path}/install/logo.png ~/.local/share/applications/
desktop-file-install --dir="$HOME/.local/share/applications"  ${usb_path}/install/jupyter.desktop

# tests
python3 ${desktop_path}/ppd/fonctions.py # imports work?
python3 ${usb_path}/install/versions.py # show version numbers

