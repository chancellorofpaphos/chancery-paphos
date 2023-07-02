"""
This code holds a class which models the letters patent pertaining to a given
peerage linked to a feudal title.
"""

# Standard imports.
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

# Local imports.
from .patent_peerage import PatentPeerage, PEERAGE_RANKS

# Local constants.
BARONY = "barony"
VISCOUNTY = "viscounty"
COUNTY = "county"
MARCH = "march"
DUCHY = "duchy"

##############
# MAIN CLASS #
##############

@dataclass
class PatentPeerageFeudal(PatentPeerage):
    """ The class in question. """
    # Class variables.
    PATH_TO_BASE: ClassVar[str] = \
        str(Path(__file__).parent/"tex"/"base_peerage_feudal.tex")
    FEE_DEGREES: ClassVar[tuple] = (BARONY, VISCOUNTY, COUNTY, MARCH, DUCHY)
    ROSES_CLAUSES: ClassVar[tuple] = ("one rose", "two roses")
    FEE_MARKER: ClassVar[str] = "#FEE_TITLE"
    FEE_DEGREE_MARKER: ClassVar[str] = "#FEE_DEGREE"
    ROSES_MARKER: ClassVar[str] = "#ROSES"

    # Fields.
    fee: str = None
    fee_degree: str = None
    roses: str = None

    def __post_init__(self):
        super().__post_init__()
        self.fee_degree = self.FEE_DEGREES[PEERAGE_RANKS.index(self.degree)]
        self.roses = self.get_roses()

    def get_roses(self):
        """ Return the correct roses clause. """
        if self.fee_degree == COUNTY:
            return self.ROSES_CLAUSES[1]
        return self.ROSES_CLAUSES[0]

    def get_special_replacement_pairs(self):
        """ Return a tuple of pairs of strings, giving the substrings to be
        replaced and their replacements, for the SPECIAL replacements that
        need to be done only for the kind of patent corresponding to this
        inheritance. """
        result = (
            (self.FEE_MARKER, self.fee),
            (self.FEE_DEGREE_MARKER, self.fee_degree),
            (self.ROSES_MARKER, self.roses)
        )
        result = result+super().get_special_replacement_pairs()
        return result
