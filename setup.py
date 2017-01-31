# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
	name='genome_update',
	version = '0.1.5',
	description = 'A script for updating a local directory with genomes, from NCBI assembly files',
	long_description = long_description,
	url='https://github.com/Emisam/genome_update.git',
	author='Emil Samuelsson',
	author_email='Emil@Samuelsson.pp.se',
	licence='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Bio-Informatics',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
	],
	packages=find_packages(),
	install_requires=['pandas', 'PyYAML'],
	entry_points={
        'console_scripts': [
            'genome_update=genome_update.__main__:main'
        ]
    }
	)