#!/bin/bash

SCRIPTS_DIR="$(pwd)/scripts"

echo "Installing venv"
$SCRIPTS_DIR/install_venv.sh

echo "Installing requirements"
$SCRIPTS_DIR/install_requirements.sh

echo "Upgrading database to the last migration"
$SCRIPTS_DIR/alembic.sh upgrade head

