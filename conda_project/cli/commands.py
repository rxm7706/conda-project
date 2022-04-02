# -*- coding: utf-8 -*-
# Copyright (C) 2022 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
import sys

from ..project import load_project, CondaProjectError


def _try(func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        return 0
    except CondaProjectError as e:
        print(str(e), file=sys.stderr)
        return 1


def prepare(args):
    project = load_project(args.directory)
    retcode = _try(project.prepare, args.force)
    return retcode


def clean(args):
    project = load_project(args.directory)
    retcode = _try(project.clean)
    return retcode
