"""
This code defines a script which installs any software required by this package
which cannot be installed via PIP.
"""

# Standard imports.
import subprocess
from pathlib import Path
from venv import EnvBuilder

# Non-standard imports.
from hosker_utils import install_apt_package

# Local imports.
from source import install_fonts

#############
# FUNCTIONS #
#############

def install_venv():
    """ Create and fill the virtual environment. """
    path_obj_to_here = Path(__file__).parent
    path_to_install_venv = str(path_obj_to_here/"install_venv.sh")
    subprocess.run(["sh", path_to_install_venv], check=True)

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    install_venv()
    install_apt_package("texlive-full")
    install_fonts()

if __name__ == "__main__":
    run()
