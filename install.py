"""
This code installs the third party software this repo requires.
"""

# Standard imports.
import glob
import subprocess

# Local imports.
import config

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

def install_multiple_via_apt(package_names):
    """ Install a given package via APT. """
    subprocess.run(
        ["sudo", "apt", "--yes", "install"]+list(package_names),
        check=True
    )

def install_pip_packages(path_to_pip_req=config.DEFAULT_PATH_TO_PIP_REQ):
    """ Install the PIP packages used in this repo. """
    subprocess.run(["pip3", "install", "-r", path_to_pip_req], check=True)

def install_fonts(
        path_to_fonts_dir=config.DEFAULT_PATH_TO_FONTS_DIR,
        path_to_system_truetype_dir=config.DEFAULT_PATH_TO_SYSTEM_TRUETYPE_DIR
    ):
    """ Install all the "True Type" font files in fonts directory. """
    filenames = glob.glob(path_to_fonts_dir+"/*.ttf")
    for filename in filenames:
        arguments = ["sudo", "cp", filename, path_to_system_truetype_dir]
        subprocess.run(arguments, check=True)

def install(
        non_python_packages=config.DEFAULT_NON_PYTHON_PACKAGES,
        path_to_pip_req=config.DEFAULT_PATH_TO_PIP_REQ
    ):
    """ Install the required software. """
    get_sudo()
    update_apt()
    install_via_apt("python3-pip")
    install_pip_packages(path_to_pip_req=path_to_pip_req)
    install_multiple_via_apt(non_python_packages)
    install_fonts()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    install()

if __name__ == "__main__":
    run()
