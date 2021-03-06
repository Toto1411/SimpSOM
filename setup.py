from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='SimpSOM',

    version='1.3.1',

    description='A lightweight Python library for Kohonen Self-Organising Maps',
    long_description=long_description,

    url='https://github.com/fcomitani/SimpSOM',
	download_url = 'https://github.com/fcomitani/SimpSOM/archive/1.3.0.tar.gz', 
    author='Federico Comitani',
    author_email='federico.comitani@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
		],

    keywords='kohoen self organising maps',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['numpy', 'matplotlib','scikit-learn'],

    extras_require={},

    entry_points={
        'console_scripts': [
            'SimpSOM=SimpSOM:main',
        ],
    },
)
