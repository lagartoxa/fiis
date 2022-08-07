#!/bin/bash

ALEMBIC_VENV_PATH="$(pwd)/backend/venv/bin/alembic"

$ALEMBIC_VENV_PATH -c backend/db/alembic/alembic.ini "${@}"

