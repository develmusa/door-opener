from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='door-opener',
    version='1.0.0',
    description='Package for opening door via RaspberryPi and Relay',
    author='Samuel Krieg',
    author_email='mail@samuelkrieg.com',
    url='https://github.com/develmusa/door-opener',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)