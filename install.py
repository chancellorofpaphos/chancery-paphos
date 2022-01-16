"""
This code installs the third party software this repo requires.
"""

# Standard imports.
import subprocess

# Local constants.
DEFAULT_PATH_TO_PIP_REQ = "pip_requirements.txt"

#############
# FUNCTIONS #
#############

def get_sudo():
    """ Get superuser privileges. """
    print("I'm going to need superuser privileges for this...")
    subprocess.run(
        ["sudo", "echo", "Superuser privileges: activate!"],
        check=True
    )

def update_apt():
    """ Update APT. """
    subprocess.run(["sudo", "apt", "update"], check=True)

def install_via_apt(package_name):
    """ Install a given package via APT. """
    subprocess.run(
        ["sudo", "apt", "--yes", "install", package_name],
        check=True
    )

def install_pip_packages(path_to_pip_req=DEFAULT_PATH_TO_PIP_REQ):
    """ Install the PIP packages used in this repo. """
    subprocess.run(["pip3", "install", "-r", path_to_pip_req], check=True)

def install():
    """ Install the required software. """
    get_sudo()
    update_apt()
    install_via_apt("python3-pip")
    install_pip_packages()
    install_via_apt("texlive-full")

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    install()

if __name__ == "__main__":
    run()
