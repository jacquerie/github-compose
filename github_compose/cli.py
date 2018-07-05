# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import click


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
@click.option('-f', '--file', 'filename', default='github-compose.yml')
def update(filename):
    """Update the repos to match the config file."""
