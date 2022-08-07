#!/bin/bash

ROOT_DIR=$(pwd)

echo "Installing venv"
$ROOT_DIR/scripts/install_venv.sh

echo "Installing requirements"
$ROOT_DIR/backend/venv/bin/pip install -r versioning/requirements.txt

