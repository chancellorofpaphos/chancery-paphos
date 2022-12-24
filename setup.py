"""
This code defines the script required by setuptools.
"""

# Non-standard imports.
from setuptools import setup

# Local constants.
PACKAGE_NAME = "chancery_paphos"
VERSION = "2.0.0"
DESCRIPTION = "His Grace's Chancery"
SCRIPT_PATHS = (
    "scripts/compile-patent", "scripts/install-fonts-chancery-paphos"
)
INSTALL_REQUIRES = ("hosker_utils",)
INCLUDE_PACKAGE_DATA = True

###################################
# THIS IS WHERE THE MAGIC HAPPENS #
###################################

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    package_dir={ PACKAGE_NAME: "source" },
    packages=[PACKAGE_NAME],
    scripts=SCRIPT_PATHS,
    install_requires=INSTALL_REQUIRES,
    include_package_data=INCLUDE_PACKAGE_DATA
)
