from setuptools import setup, find_packages
from typing import List
import warnings
warnings.simplefilter('ignore')

project_name = 'Movie Recommender'
version = '1.0.0'
author = 'Ranjit Kundu'
description = 'Movie recommender system with 5000 movie base'


def get_req_list() -> List[str]:
    with open('requirements.txt') as obj:
        requirements_list = obj.readlines()
        requirements_list = [i.replace('\n', '') for i in requirements_list]
        if '-e .' in requirements_list:
            requirements_list.remove('-e .')
        return requirements_list


setup(
    name=project_name,
    version=version,
    author=author,
    description=description,
    packages=find_packages(),
    install_requires=get_req_list()
)