#!/usr/bin/env bash

apt -y update
apt -y install python3
apt -y install python3-pip
pip3 install totex
apt -y install texlive-latex-base

cd /pdf-creation
python3 tex_gen.py
cd artifacts
pdflatex generated.tex

exit
