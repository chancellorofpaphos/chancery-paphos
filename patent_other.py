"""
This code holds a class which models a given letters patent of "other" type.
"""

# Local imports.
import constants

##############
# MAIN CLASS #
##############

class PatentOther:
    """ The class in question. """
    def __init__(self, pino, day, month, year, filling):
        self.pino = pino
        self.day = get_ordinal(day)
        self.month = month
        self.year = get_ordinal(year)
        self.filling = filling

####################
# HELPER FUNCTIONS #
####################

def get_ordinal(index):
    """ Looks up the result in constants.py """
    result = constants.ordinals[index]
    return result
