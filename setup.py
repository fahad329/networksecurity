'''
The setup.py file is a crucial component in Python package distributions. 
It serves as the entry point and configuration file for packaging and 
distributing Python projects. This file provides essential metadata about 
the package,specifies its dependencies, and defines how the package should 
be installed, built, and distributed

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This function will return list of requirements"""

    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirements = line.strip()
                #Ignoring empty lines and -e .
                if requirements and requirements!='-e .':
                    requirements_lst.append(requirements)
    
    except FileNotFoundError:
        print('Requirements.txt not found')
    
    return requirements_lst

setup(
    name="Network Security",
    version="1.0.0",
    author="Fahad Farooq",
    author_email="kh_fahad_farooq@yahoo.com",
    packages=find_packages(),
    install_requires=get_requirements()
)