# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

import click
import six
import yaml
from dotenv import load_dotenv
from github import Github, UnknownObjectException


@click.group()
@click.version_option()
def cli():
    load_dotenv()


@cli.command()
@click.option('-f', '--file', 'filename', default='github-compose.yml')
def update(filename):
    """Update the repos to match the config file."""
    with open(filename, 'r') as fd:
        config = yaml.load(fd)

    github_user = os.getenv('GITHUB_USER')
    github_pass = os.getenv('GITHUB_PASS')
    github = Github(github_user, github_pass)

    for orgname, org in six.iteritems(config['orgs']):
        organization = github.get_organization(orgname)
        for reponame, repo in six.iteritems(org['repos']):
            try:
                repository = organization.get_repo(reponame)
            except UnknownObjectException:
                repository = organization.create_repo(reponame)

            if repo:
                kwargs = {'description': repo.get('description', '')}
                repository.edit(**kwargs)
