# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

import click
import six
import yaml
from dotenv import find_dotenv, load_dotenv
from github3 import GitHub, GitHubError


@click.group()
@click.version_option()
def cli():
    load_dotenv(find_dotenv(usecwd=True))


@cli.command()
@click.option('-f', '--file', 'filename', default='github-compose.yml')
def update(filename):
    """Update the repos to match the config file."""
    with open(filename, 'r') as fd:
        config = yaml.load(fd)

    github_user = os.getenv('GITHUB_USER')
    github_pass = os.getenv('GITHUB_PASS')
    github = GitHub(github_user, github_pass)

    for orgname, org in six.iteritems(config['orgs']):
        organization = github.organization(orgname)
        for reponame, repo in six.iteritems(org['repos']):
            try:
                repository = github.repository(orgname, reponame)
            except GitHubError:
                repository = organization.create_repository(reponame)

            if repo:
                kwargs = {'description': repo.get('description', '')}
                repository.edit(reponame, **kwargs)
