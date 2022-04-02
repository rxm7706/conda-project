# -*- coding: utf-8 -*-
# Copyright (C) 2022 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from argparse import ArgumentParser
from conda_project import __version__

from . import commands


def cli(args=None):
    common = ArgumentParser(add_help=False)
    common.add_argument(
        '--directory',
        metavar='PROJECT_DIR',
        default='.',
        help="Project directory (defaults to current directory)"
    )

    p = ArgumentParser(
        description="Tool for encapsulating, running, and reproducing projects with Conda environments",
        conflict_handler='resolve',
    )
    p.add_argument(
        '-V', '--version',
        action='version',
        help='Show the conda-prefix-replacement version number and exit.',
        version="conda_project %s" % __version__,
    )

    subparsers = p.add_subparsers(metavar='command', required=True)

    create_prepare_parser(subparsers, common)
    create_clean_parser(subparsers, common)

    args, unknown = p.parse_known_args(args)

    args.func(args)


def create_prepare_parser(subparsers, parent_parser):
    desc = 'Prepare the Conda environments'

    p = subparsers.add_parser(
        'prepare',
        description=desc,
        help=desc,
        parents=[parent_parser]
    )
    p.add_argument(
        '--force',
        help='Remove and recreate an existing environment.',
        action='store_true'
    )

    p.set_defaults(func=commands.prepare)


def create_clean_parser(subparsers, parent_parser):
    desc = 'Clean the Conda environments'

    p = subparsers.add_parser(
        'clean',
        description=desc,
        help=desc,
        parents=[parent_parser]
    )

    p.set_defaults(func=commands.clean)


def main():
    import sys

    if len(sys.argv) == 1:
        cli(('-h',))

    cli(sys.argv[1:])
