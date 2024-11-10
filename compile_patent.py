"""
This code defines a script which generates a letters patent given an input file.
"""

# Standard imports.
from pathlib import Path

# Bespoke imports.
from source import MachineInterface

# Local constants.
PATH_TO_INPUT = str(Path(__file__).parent/"input.json")
PATH_TO_EXAMPLES = str(Path(__file__).parent/"example_input_files")

####################
# HELPER FUNCTIONS #
####################

def check_input() -> bool:
    """ Check that the input file exists. """
    if Path(PATH_TO_INPUT).exists():
        return True
    print("Looks like there's no input file at: %s" % PATH_TO_INPUT)
    print("Create an input.json file in the same directory as this script,")
    print("and try again.")
    print("(See %s for examples.)" % PATH_TO_EXAMPLES)
    return False

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    if check_input():
        interface = MachineInterface(PATH_TO_INPUT)
        interface.generate()

if __name__ == "__main__":
    run()
