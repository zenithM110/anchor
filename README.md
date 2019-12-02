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

Before installing `anchor`, you will need to set the `AIRES_RUN_DIR` environment variable telling `zhaires.py` (the low-level Aires wrapper package) where to store the Aires/ZHAireS output files. Each simulated shower is created in its own directory under `AIRES_RUN_DIR` with the name of the Aires task.

    $ export AIRES_RUN_DIR=<path to directory with decent storage capacity>
    
This should be added to your `.{bash,zsh,fish,tcsh,c}rc` file if you plan on regularly using `anchor` or `zhaires.py`.

The recommended method of installation is to first clone the package

    # git clone https://github.com/rprechelt/anchor
	
and then change into the cloned directory and install using `pip`

    # cd anchor
    # pip install --user -e .
	
We now need to install the various Aires/ZHAireS binaries that `anchor` uses to perform the shower simulations. Change into the `anchor/aires` directory. You will need to ensure that the following tree structure is recreated (if you are a member of ANITA, contact @rprechelt).

    # cd anchor/aires/
	# ls
	    sources/
    # ls sources/
        Aires.2-8-4a.tar.gz
        ZHAireS-betav28r18c-loopfresnel.tar
        ZHAireS-betav28r18c-Upgoing.tar
        ZHAireS-betav28r21-ANITA-reflected-beta0.2-Frcoeffs.tar
        ZHAireS-betav28r24-RASPASS.tar
		
Once all the above tar-balls are in place, you can then run

    # ./setup.sh
	
from the `anchor/aires` directory. This will compile all four versions of ZHAireS (this may take ~5 minutes).

You should then make sure that the installation was successful by trying to import `anchor`

    # python -c 'import anchor'

If you wish to develop new features in `anchor`, you will also need to install some additional dependencies so you can run our unit tests

    # pip install --user -e .[test]
	
Once that is completed, you can run the unit tests directory from the `anchor` directory

    # python -m pytest tests


