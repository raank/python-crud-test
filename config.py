import os
import click
import sys
import env_file

envs = env_file.get('.env')

configs = {
    'env': envs.get('APP_ENV'),
    'database': envs.get('DATABASE'),
    'database_tests': envs.get('DATABASE_TESTS'),
    'entity_default': envs.get('ENTITY_DEFAULT'),
    'action_default': envs.get('ACTION_DEFAULT'),
    'export_path': envs.get('EXPORT_PATH')
}

def get(name):
    if configs.get(name):
        return configs.get(name)
    
    return False
