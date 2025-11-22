#!/bin/bash


sudo apt update

sudo apt install -y python3 python3-pip python3-venv


python3 -m venv .pydantic_venv

source .pydantic_venv/bin/activate

pip install --upgrade pip
pip install pydantic

echo "=== install pydantic done! ==="

