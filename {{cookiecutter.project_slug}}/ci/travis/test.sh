#!/bin/sh

pip install .
rm -r {{ cookiecutter.project_slug }}
python -m pytest tests/*