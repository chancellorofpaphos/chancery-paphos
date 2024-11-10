"""
This code defines a machine interface class, with which code can create and use
an object of the Patent-type class.
"""

# Standard imports.
import json
from dataclasses import dataclass, field

# Local imports.
from .patent import Patent
from .patent_peerage import PatentPeerage
from .patent_peerage_feudal import PatentPeerageFeudal

# Local constants.
PATENT_TYPE_KEY = "type"
PEERAGE_TYPE = "peerage"
PEERAGE_FEUDAL_TYPE = "peerage-feudal"

##############
# MAIN CLASS #
##############

@dataclass
class MachineInterface:
    """ The class in question. """
    path_to_input_file: str
    patent_obj: Patent|PatentPeerage|PatentPeerageFeudal|None = \
        field(init=False, default=None)

    def __post_init__(self):
        self._set_patent_obj()

    def _set_patent_obj(self):
        """ Make the patent object, given the input file. """
        with open(self.path_to_input_file, "r") as input_file:
            input_dict = json.loads(input_file.read())
        patent_type = input_dict.pop(PATENT_TYPE_KEY)
        if patent_type == PEERAGE_FEUDAL_TYPE:
            result = PatentPeerageFeudal(**input_dict)
        elif patent_type == PEERAGE_TYPE:
            result = PatentPeerage(**input_dict)
        else:
            result = Patent(**input_dict)
        self.patent_obj = result

    def generate(self):
        """ Generate the output. """
        self.patent_obj.generate()
