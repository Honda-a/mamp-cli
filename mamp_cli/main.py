"""
py_pkg.entry_points.py
~~~~~~~~~~~~~~~~~~~~~~

This module contains the entry-point functions for the py_pkg module,
that are referenced in setup.py.
"""

import click
# from mamp_cli.api import *
# from mamp_cli.tools import mamp


@click.group()
def cli1():
    pass


@cli1.command()
def cmd1():
    """Command on cli1"""


@cli1.command()
def cli1_cmd2():
    """Command on cli1"""


@click.group()
def cli2():
    pass


@cli2.command()
def cmd2():
    """Command on cli2"""


mamp_cli = click.CommandCollection(sources=[cli1, cli2])

if __name__ == '__main__':
    mamp_cli()
