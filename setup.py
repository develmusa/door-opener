from setuptools import setup, find_packages, Command

# Package meta-data.
NAME = 'door-opener'
DESCRIPTION = 'Package for opening door via RaspberryPi and Relay.'
URL = 'https://github.com/develmusa/door-opener'
EMAIL = 'mail@samuelkrieg.com'
AUTHOR = 'Samuel Krieg'
REQUIRES_PYTHON = '>=3.2.0'
VERSION = '1.0.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'bottle',
]

class InstallCommand(Command):
    """Support setup.py upload."""

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    cmdclass={
        'install': InstallCommand,
    },
)