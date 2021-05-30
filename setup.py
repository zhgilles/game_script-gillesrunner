from setuptools import setup

with open('requirements.txt') as f:
    requires = f.read()
    requires = requires.split('\n')
    requires = [i for i in requires if i]

with open('README.md', 'r') as fh:
    long_description = fh.read()

gilles_package = []

setup(
    name='gillesrunner',
    url='',
    install_requires=requires + gilles_package,
    package_data={},
    long_description=long_description,
)