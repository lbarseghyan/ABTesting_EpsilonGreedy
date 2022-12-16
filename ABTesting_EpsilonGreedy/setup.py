#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


requirements = ['pandas', 'numpy', 'matplotlib.pyplot', 'matplotlib']


setup(
    author="Laura Barseghyan",
    author_email='barseghyanlaura1@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: MIT License '
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Python package for A/B Testing with Epsilon Greedy algorithm.",
    install_requires= requirements,
    name='ABTesting_EpsilonGreedy',
    packages=find_packages(include=['ABTesting_EpsilonGreedy', 'ABTesting_EpsilonGreedy.*']),
    version='0.1.0'
)
