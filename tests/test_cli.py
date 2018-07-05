# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from github_compose.cli import cli


def test_update(runner):
    result = runner.invoke(cli, ['update'])

    assert 0 == result.exit_code
