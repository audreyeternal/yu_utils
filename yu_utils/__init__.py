# -*- coding: utf-8 -*-

"""Top-level package for yu_utils."""

__author__ = "eternalaudrey"
__email__ = "eternalaudrey@gmail.com"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0.0.1"


def get_module_version():
    return __version__


from .example import Example  # noqa: F401
