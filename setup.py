#!/usr/bin/env python3
import io
from setuptools import setup


with io.open('README.md', encoding='utf-8') as f:
    README = f.read()

with io.open('HISTORY.md', encoding='utf-8') as f:
    HISTORY = f.read()


setup(
    name='Flask-Redis',
    version='0.1',
    url='https://github.com/imcery/flask-redis',
    author='Pavel Saparov',
    author_email='info@imcery.com',
    maintainer='Pavel Saparov',
    maintainer_email='info@imcery.com',
    download_url='https://github.com/imcery/flask-redis/releases',
    description='Redis Extension for Flask Applications',
    long_description=README + '\n\n' + HISTORY,
    packages=['flask_redis'],
    package_data={'': ['LICENSE']},
    zip_safe=False,
    install_requires=[
        'Flask>=0.9',
        'redis>=2.10',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
