#!/usr/bin/env python3

import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='pgsql_connector',
    version='0.0.1',
    author='Oleg Maslennikov',
    author_email='maslolpavl@gmail.com',
    description='usefull tools for pg sql',
    url='https://github.com/Ilwapoi/pgsql_connector',
    license='MIT',
    packages=['pgsql_connector'],
    install_requires=['pandas','psycopg2','numpy'],
)