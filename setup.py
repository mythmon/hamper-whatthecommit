from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='whatthecommit',
    version='0.1',
    packages=['whatthecommit'],
    author='Mike cooper',
    author_email='mythmon@elem.us',
    url='https://github.com/mythmon/hamper-whatthecommit',
    install_requires=requirements,
    package_data={'whatthecommit': ['requirements.txt', 'README.rst', 'LICENSE']},
    entry_points={
        'hamperbot.plugins': [
            'whatthecommit = whatthecommit:WhatTheCommit'
        ],
    },
)
