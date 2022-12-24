"""
This code defines some functions which handle the fonts used by this package.
"""

# Standard imports.
import shutil
import subprocess
from pathlib import Path

# Local constants.
PATH_TO_PACKAGE_FONTS_FOLDER = str(Path(__file__).parent/"fonts")
PATH_TO_HOME_FONTS_FOLDER = str(Path.home()/".fonts")

#############
# FUNCTIONS #
#############

def install_fonts():
    """ Install the fonts used by this package. """
    path_obj_to_source = Path(PATH_TO_PACKAGE_FONTS_FOLDER)
    path_obj_to_dest = Path(PATH_TO_HOME_FONTS_FOLDER)
    path_obj_to_dest.mkdir(parents=True, exist_ok=True)
    for path_obj in path_obj_to_source.glob("*"):
        if path_obj.is_dir():
            shutil.copytree(
                str(path_obj), str(path_obj_to_dest), dirs_exist_ok=True
            )
