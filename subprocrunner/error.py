# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, unicode_literals


class CommandError(Exception):
    pass


class InvalidCommandError(CommandError):
    pass


class CommandNotFoundError(CommandError):
    pass