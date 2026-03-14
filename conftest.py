import requests
import os
from glob import glob
from os.path import join
from pathlib import Path
from pytest import fixture
from dotenv import load_dotenv
from platform import system

load_dotenv()


def get_fixtures():
    """Подключаем фикстуры к проекту"""
    fixtures = join(Path(__file__).parent, 'fixtures')
    file_path = []
    for file in glob(f'{fixtures}/*.py'):
        file = file.split('/') if system().lower() in ['linux', 'darwin'] else file.split('\\')
        file = file[-1].split('.')[0]
        if file not in ['__init__', '__pycache__']:
            file_path.append(f'fixtures.{file}')
    print(f'Подключаем фикстуры: {file_path}')        
    return file_path

pytest_plugins = get_fixtures() # Подключаем все фикстуры к проекту




