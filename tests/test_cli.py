# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import pytest

from github_compose.cli import cli

ONE_ORG_ONE_REPO = '''\
orgs:
  foo-org:
    repos:
      bar-repo:
        description: "Description of the bar repo."
'''

ONE_ORG_ONE_REPO_WITHOUT_DESCRIPTION = '''\
orgs:
  foo-org:
    repos:
      bar-repo:
'''

ONE_ORG_TWO_REPOS = '''\
orgs:
  foo-org:
    repos:
      bar-repo:
        description: "Description of the bar repo."
      baz-repo:
        description: "Description of the baz repo."
'''


@pytest.mark.vcr()
def test_update_uses_the_provided_filename(runner, tmpdir):
    config_fd = tmpdir.join('github-compose.yaml')
    config_fd.write(ONE_ORG_ONE_REPO)

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code


@pytest.mark.vcr()
def test_update_does_not_require_a_repository_description(runner, tmpdir):
    config_fd = tmpdir.join('github-compose.yml')
    config_fd.write(ONE_ORG_ONE_REPO_WITHOUT_DESCRIPTION)

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code


@pytest.mark.vcr()
def test_update_creates_a_repository_if_it_does_not_exist(runner, tmpdir):
    config_fd = tmpdir.join('github-compose.yml')
    config_fd.write(ONE_ORG_TWO_REPOS)

    result = runner.invoke(cli, ['update', '-f', str(config_fd)])

    assert 0 == result.exit_code
