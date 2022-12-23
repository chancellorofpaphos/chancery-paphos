"""
This code tests that patent files are being generated.
"""

# Local imports.
from pathlib import Path

# Source imports.
from source import MachineInterface

# Local constants.
PATH_OBJ_TO_TEST_FILES = Path(__file__).parent/"test_files"
PATH_TO_INPUT_PEERAGE = str(PATH_OBJ_TO_TEST_FILES/"input_peerage.json")
PATH_TO_INPUT_OTHER = str(PATH_OBJ_TO_TEST_FILES/"input_other.json")
EXPECTED_PATH_TO_OUTPUT = "out.pdf"

###########
# TESTING #
###########

def test_generate_patent_peerage():
    """ Test (1) that the code runs without raising an exception, and (2) that
    at least some sort of output file is being generated. """
    interface = MachineInterface(PATH_TO_INPUT_PEERAGE)
    interface.generate()
    path_obj = Path(EXPECTED_PATH_TO_OUTPUT)
    assert path_obj.exists()
    path_obj.unlink() # Tidy up.

def test_generate_patent_other():
    """ Test (1) that the code runs without raising an exception, and (2) that
    at least some sort of output file is being generated. """
    interface = MachineInterface(PATH_TO_INPUT_OTHER)
    interface.generate()
    path_obj = Path(EXPECTED_PATH_TO_OUTPUT)
    assert path_obj.exists()
    path_obj.unlink() # Tidy up.
