"""
This code defines a script which runs this repo's continuous integration
routines.
"""

# Standard imports.
import glob
import subprocess

# Non-standard imports.
import pytest

# Local constants.
DEFAULT_MIN_CODE_COVERAGE = 70
DEFAULT_MIN_LINT_SCORE = 9

#############
# FUNCTIONS #
#############

def run_unit_tests(min_code_coverage=DEFAULT_MIN_CODE_COVERAGE):
    """ Run PyTest. """
    arguments = [
        "--cov-report", "term",
        "--cov-fail-under="+str(min_code_coverage),
        "--cov=."
    ]
    return_code = pytest.main(arguments)
    assert return_code == 0, "PyTest returned code: "+str(return_code)

def run_linter(min_lint_score=DEFAULT_MIN_LINT_SCORE):
    """ Run PyLint, checking that all the files, taken as a WHOLE, reach a
    given score. """
    files = glob.glob("*.py")
    arguments = ["pylint", "--fail-under="+str(min_lint_score)]+files
    subprocess.run(arguments, check=True)

def run_continuous_integration():
    """ Run the continuous integration routines. """
    run_unit_tests()
    run_linter()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    run_continuous_integration()

if __name__ == "__main__":
    run()
