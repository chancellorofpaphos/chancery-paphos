"""
This code holds a class which models a given letters patent of "other" type.
"""

# Standard imports.
from dataclasses import dataclass

# Local imports.
import config

# Local imports.
DEFAULT_PATH_TO_BASE = "base_other.tex"

##############
# MAIN CLASS #
##############

@dataclass
class PatentOther:
    """ The class in question. """
    pino: int = 0
    day: int = 0
    month: str = None
    year: int = 0
    filling: str = None

    def build_object(self):
        """ Fill this object's fields with something sensible. """
        self.day = get_ordinal(self.day)
        self.year = get_ordinal(self.year)

    def make_main(
            self,
            path_to_base=DEFAULT_PATH_TO_BASE,
            path_to_main=config.DEFAULT_PATH_TO_MAIN,
            encoding=config.DEFAULT_ENCODING
        ):
        """ Make the main file of LaTeX code. """
        with open(path_to_base, "r", encoding=encoding) as base_file:
            main = base_file.read()
        main = main.replace("#PINO", str(self.pino))
        main = main.replace("#DAY", str(self.day))
        main = main.replace("#MONTH", self.month)
        main = main.replace("#YEAR", str(self.year))
        main = main.replace("#FILLING", self.filling)
        with open(path_to_main, "w", encoding=encoding) as main_file:
            main_file.write(main)

    def build(self):
        """ Build this object and then make the main file. """
        self.build_object()
        self.make_main()

####################
# HELPER FUNCTIONS #
####################

def get_ordinal(index):
    """ Looks up the result in constants.py """
    result = config.ORDINALS[index]
    return result
