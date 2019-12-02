from setuptools import setup, find_packages
from os import path

# get the absolute path of this project
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# the standard setup info
setup(
    name='anchor',
    version="0.1.0",
    description=("A Cosmic Ray Air Shower Creator for "
                 "the Antarctic Impulsive Transient Antenna"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rprechelt/anchor',
    author='Remy L. Prechelt',
    author_email='prechelt@hawaii.edu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='anita cosmic ray air shower simulator physics radio neutrino',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.6*, <4',
    install_requires=['numpy', 'pyIGRF',
                      'zhaires @ git+git://github.com/rprechelt/zhaires.py'],
    extras_require={
        'test': ['pytest', 'coverage'],
    },
    project_urls={
    },
)
