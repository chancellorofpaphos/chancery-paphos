"""
This code defines a script which installs any software required by this package
which cannot be installed via PIP.
"""

# Non-standard imports.
from hosker_utils import install_apt_package

# Local imports.
from source import install_fonts

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    install_apt_package("texlive-full")
    install_fonts()

if __name__ == "__main__":
    run()
