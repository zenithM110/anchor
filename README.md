# Anchor

A Cosmic Ray Air Shower Creator for the Antarctic Impulsive Transient Antenna (ANITA).

[![Actions Status](https://github.com/rprechelt/anchor/workflows/tests/badge.svg)](https://github.com/rprechelt/anchor/actions)
![GitHub](https://img.shields.io/github/license/rprechelt/anchor?logoColor=brightgreen)
![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue)

Anchor (**AN**ITA **C**osmic-Ray S**ho**wer Creat**or**) is a utility to automate the generation of cosmic ray shower templates for the Antarctic Impulsive Transient Antenna (ANITA). Anchor handles the raytracing, event setup, and Aires configuration necessary for all three primary classes of ANITA events (reflected, stratospheric, and upgoing events). Anchor also supports direct downgoing air showers (as would be used for ground radio arrays).

Anchor does not include the various ZHAireS versions needed to run the various simulations (it is a high-level wrapper). If you are member of the ANITA collaboration, contact @rprechelt on Slack for all the files you need. Otherwise, you will need to contact the authors of ZHAireS (anchor currently uses the following ZHAireS versions: `28r18c-loopfresnel`, `28r18c-Upgoing`, `28r21-ANITA-reflected`, and `28r24-RASPASS`). See the Aires [install script](aires/setup.sh) for details.

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


