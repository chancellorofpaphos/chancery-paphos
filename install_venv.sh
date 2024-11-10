#!/bin/sh

### This code creates the virtual environment and fills it.

set -e  # Crash on the first non-zero exit code.

# Local constants.
PATH_TO_HERE=$(realpath $(dirname $0))
PATH_TO_VENV="$PATH_TO_HERE/venv"

# Let's get cracking.
cd $PATH_TO_HERE
if [ ! -d $PATH_TO_VENV ]; then
    python3 -m venv $PATH_TO_VENV
fi
. venv/bin/activate
pip install -r requirements.txt
deactivate
