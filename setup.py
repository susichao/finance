from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup( 
name = 'ML-project',
version = '0.0.1',
author = 'Srija Dutta',
description = 'A project for machine learning to predict the malicious data.',
author_email = 'srijadutta0420@gmail.com',
packages = find_packages(),
install_requires=get_requirements('requirements.txt')
)