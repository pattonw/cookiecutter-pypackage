# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'
__version_info__ = tuple(int(n) for n in __version__.split('.'))

from .{{ cookiecutter.project_slug }} import get_42

__all__ = ["get_42"]
