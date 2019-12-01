# anchor

A Cosmic Ray Air Shower Creator for the Antarctic Impulsive Transient Antenna

[![Actions Status](https://github.com/rprechelt/anchor/workflows/CI/badge.svg)](https://github.com/rprechelt/anchor/actions)
![GitHub](https://img.shields.io/github/license/rprechelt/anchor?logoColor=brightgreen)
![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)

### Installation

To install `anchor`, you will need `git` and Python >= 3.6. All three should be available in the package manager of any modern OS. It is tested on macOS 10.14, ubuntu 18.04, ubuntu 16.04, Fedora 29, and Fedora 30.

The below instructions are assuming that `python` refers to Python 3.\*. If `python` still refers to a decrepit Python 2.\*, please replace `python` with `python3` and `pip` with `pip3`.

The recommended method of installation is to first clone the package

    # git clone https://github.com/rprechelt/anchor
	
and then change into the cloned directory and install using `pip`

    # cd anchor
    # pip install --user -e .
	
You should then make sure that the installation was successful by trying to import `anchor`

    # python -c 'import anchor'

If you wish to develop new features in `anchor`, you will also need to install some additional dependencies so you can run our unit tests

    # pip install --user -e .[test]
	
Once that is completed, you can run the unit tests directory from the `anchor` directory

    # python -m pytest tests


