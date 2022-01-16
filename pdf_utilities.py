"""
This code defines some utilities for making and working with PDFs.
"""

# Standard imports.
import os
import subprocess

# Local imports.
import config

#############
# FUNCTIONS #
#############

def make_pdf(path_to_output=config.DEFAULT_PATH_TO_OUTPUT):
    """ Build a PDF from main.tex using LaTeX, and then tidy up. """
    subprocess.run(["xelatex", "main.tex"], check=True)
    subprocess.run(["cp", "main.pdf", path_to_output], check=True)
    for item in ["main.aux", "main.log", "main.pdf", "main.tex"]:
        os.remove(item)
