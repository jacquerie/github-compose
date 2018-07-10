# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest

from github_compose.cli import cli

SIMPLE = '''\
orgs:
  foo-org:
    repos:
      bar-repo:
        description: "Description of the bar repo."
'''


@pytest.mark.vcr()
def test_update_uses_the_provided_filename(runner, tmpdir):
    config_fd = tmpdir.join('github-compose.yaml')
    config_fd.write(SIMPLE)

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code
