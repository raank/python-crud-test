import os
import click
import datetime
import env_file
import sys

from app.console import Console

@click.command()
@click.option('--model', '-m', 'model', required=False, help="Define entity")
@click.option('--action', '-a', 'action', required=False, help="Define mode of operation")
@click.argument('id', required=False)

def process(model, action, id):
    Console(model, action, id)

if __name__ == '__main__':
    process()