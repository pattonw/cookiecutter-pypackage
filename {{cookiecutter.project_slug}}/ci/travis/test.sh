#!/bin/sh

pip install .
rm -r {{ cookiecutter.project_slug }}
{%- if cookiecutter.use_pytest == 'y' %}
python -m pytest tests
{%- else %}
python -m unittest tests
{%- endif %}