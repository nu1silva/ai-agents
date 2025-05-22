#!/bin/bash

# check if the virtual environment already exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment 'venv'..."
    python3 -m venv venv
else
    echo "Virtual environment 'venv' already exists. Activating it..."
fi

# activate the virtual environment
echo "source venv/bin/activate"