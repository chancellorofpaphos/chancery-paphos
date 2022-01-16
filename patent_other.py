"""
This code holds a class which models a given letters patent of "other" type.
"""

# Standard imports.
import os
import subprocess
from dataclasses import dataclass
from typing import ClassVar

# Local imports.
import config

##############
# MAIN CLASS #
##############

@dataclass
class PatentOther:
    """ The class in question. """
    # Fields.
    pino: int = 0
    day: int = 0
    month: str = None
    year: int = 0
    filling: str = None
    addenda: tuple = None

    # Class attributes.
    ENCODING: ClassVar[str] = config.DEFAULT_ENCODING
    PATH_TO_BASE: ClassVar[str] = "base_other.tex"
    PATH_TO_MAIN: ClassVar[str] = config.DEFAULT_PATH_TO_MAIN
    PATH_TO_OUTPUT: ClassVar[str] = config.DEFAULT_PATH_TO_OUTPUT

    def build_object(self):
        """ Fill this object's fields with something sensible. """
        self.day = get_ordinal(self.day)
        self.year = get_ordinal(self.year)

    def make_main(self):
        """ Make the main file of LaTeX code. """
        with open(self.PATH_TO_BASE, "r", encoding=self.ENCODING) as base_file:
            main = base_file.read()
        main = main.replace("#PINO", str(self.pino))
        main = main.replace("#DAY", str(self.day))
        main = main.replace("#MONTH", self.month)
        main = main.replace("#YEAR", str(self.year))
        main = main.replace("#FILLING", self.filling)
        with open(self.PATH_TO_MAIN, "w", encoding=self.ENCODING) as main_file:
            main_file.write(main)

    def make_pdf(self):
        """ Build a PDF from main.tex using LaTeX, and then tidy up. """
        subprocess.run(["xelatex", self.PATH_TO_MAIN], check=True)
        subprocess.run(["cp", "main.pdf", self.PATH_TO_OUTPUT], check=True)
        for item in ["main.aux", "main.log", "main.pdf", "main.tex"]:
            os.remove(item)

    def add_addendum(self, path_to_addendum):
        """ Add a given document to the end of the output. """
        path_to_temp = "temp.pdf"
        arguments = [
            "pdfunite", self.PATH_TO_OUTPUT, path_to_addendum, path_to_temp
        ]
        subprocess.run(arguments, check=True)
        os.remove(self.PATH_TO_OUTPUT)
        os.rename(path_to_temp, self.PATH_TO_OUTPUT)

    def add_addenda(self):
        """ Add any extra pages onto the end of the patent. """
        if not self.addenda:
            return
        for path_to in self.addenda:
            self.add_addendum(path_to)

    def build(self):
        """ Build this object and then make the main file. """
        self.build_object()
        self.make_main()
        self.make_pdf()
        self.add_addenda()

####################
# HELPER FUNCTIONS #
####################

def get_ordinal(index):
    """ Looks up the result in constants.py """
    result = config.ORDINALS[index]
    return result
