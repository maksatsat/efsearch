from setuptools import setup, find_packages

def get_requires():
    reqs = []
    for line in open('requirements.txt', 'r').readlines():
        reqs.append(line)
    return reqs

setup(

    name="efsearch",

    version="0.1",

    packages=find_packages(),

    install_requires =  get_requires()
)
