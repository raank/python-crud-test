import os
import click
import datetime
import env_file
import sys

from app.service import Crud
from app.model import Client, Product

envs = env_file.get('.env')

@click.command()

@click.option(
    '--model', '-m', 'model',
    required=False, help="Define entity")

@click.option(
    '--action', '-a', 'action',
    required=False, help="Define mode of operation"
)

@click.option(
    '--id', '-i', 'id',
    required=False
)

@click.option(
    '--export', '-i', 'export',
    required=False
)

def process(model, action, id=None, export=False):
    actions = ('index', 'store', 'show', 'update', 'delete', 'export')
    
    if model is None:
        model = envs.get('ENTITY_DEFAULT')
    
    if action is None and id:
        action = 'show'
    elif action is None and id is None:
        action = envs.get('ACTION_DEFAULT')
        
    if action not in actions:
        print('Action is not enabled')
        os.abort()
        
    if model == 'products':
        entity = Product()
    else:
        entity = Client()
    
    service = Crud(entity, action)
    
    try:
        crudObj = getattr(service, action)
        
        if id:
            runner = crudObj(id)
        else:
            runner = crudObj()
            
        print(runner)
    except Exception as err:
        print('Fail: %s' % err)

if __name__ == '__main__':
    process()