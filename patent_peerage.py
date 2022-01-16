"""
This code holds a class which models the letters patent pertaining to a
given peerage.
"""

# Standard imports.
from dataclasses import dataclass
from typing import ClassVar

# Local imports.
import config
from patent_other import PatentOther, get_ordinal

##############
# MAIN CLASS #
##############

@dataclass
class PatentPeerage(PatentOther):
    """ The class in question. """
    # Fields.
    grantee: str = None
    gender: str = None
    degree: str = None
    title: str = None
    subsidiary_titles: tuple = None
    whereas: str = None
    remainder: str = None
    pronoun_nominative: str = None
    pronoun_dative: str = None
    pronoun_possessive: str = None
    advance_clause: str = None
    trusty_clause: str = None
    state_clause: str = None
    dignify_clause: str = None
    third_invocation: str = None
    rights_clause: str = None
    degree_clause: str = None
    degree_plural: str = None

    # Class attributes.
    PATH_TO_BASE: ClassVar[str] = "base_peerage.tex"

    def build_object(self):
        """ Fill the fields of this object with something sensible. """
        self.day = get_ordinal(self.day)
        self.year = get_ordinal(self.year)
        self.subsidiary_titles = \
            get_subsidiary_titles(self.subsidiary_titles)
        self.pronoun_nominative = self.get_pronoun_nominative()
        self.pronoun_dative = self.get_pronoun_dative()
        self.pronoun_possessive = self.get_pronoun_possessive()
        self.advance_clause = self.get_advance_clause()
        self.trusty_clause = self.get_trusty_clause()
        self.state_clause = self.get_state_clause()
        self.dignify_clause = self.get_dignify_clause()
        self.third_invocation = self.get_third_invocation()
        self.remainder = self.get_remainder()
        self.rights_clause = self.get_rights_clause()
        self.degree_clause = self.get_degree_clause()
        self.degree_plural = self.get_degree_plural()

    def get_pronoun_nominative(self):
        """ Looks up the result in config.py. """
        return config.PRONOUNS_NOMINATIVE[self.gender]

    def get_pronoun_dative(self):
        """ Looks up the result in config.py. """
        return config.PRONOUNS_DATIVE[self.gender]

    def get_pronoun_possessive(self):
        """ Looks up the result in config.py. """
        return config.PRONOUNS_POSSESSIVE[self.gender]

    def get_advance_clause(self):
        """ Looks up the result in config.py. """
        if self.degree == "baronet":
            return config.ADVANCE_CLAUSES["baronet"]
        return config.ADVANCE_CLAUSES["peer"]

    def get_trusty_clause(self):
        """ Looks up the result in config.py. """
        if self.degree == "baronet":
            return ""
        return config.TRUSTY_CLAUSES[self.degree]

    def get_state_clause(self):
        """ Looks up the result in config.py. """
        if self.degree == "baronet":
            return config.STATE_CLAUSES["baronet"]
        return config.STATE_CLAUSES["peer"]

    def get_dignify_clause(self):
        """ Looks up the result in config.py. """
        if self.degree in ("duke", "marquess", "earl"):
            if self.gender == "female":
                result = config.DIGNIFY_CLAUSES["female"]+self.title+", "
            else:
                result = config.DIGNIFY_CLAUSES[self.degree]
        else:
            result = ""
        return result

    def get_third_invocation(self):
        """ Constructs the third invocation of the title granted. """
        if self.degree in config.NAME_CLAUSES:
            result = config.NAME_CLAUSES[self.degree]+self.title
        else:
            result = ""
        return result

    def get_remainder(self):
        """ Looks up the result in config.py, or not. """
        if self.remainder in config.STANDARD_REMAINDERS:
            result = config.STANDARD_REMAINDERS[self.remainder]
        else:
            result = self.remainder
        result = result.replace("#POSSESSIVE", self.pronoun_possessive)
        return result

    def get_rights_clause(self):
        """ Looks up the result in config.py. """
        if self.degree == "baronet":
            result = config.RIGHTS_CLAUSES["baronet"]
        else:
            result = config.RIGHTS_CLAUSES["peer"]
        return result

    def get_degree_clause(self):
        """ Looks up the result in config.py. """
        return config.DEGREE_CLAUSES[self.degree]

    def get_degree_plural(self):
        """ Looks up the result in config.py. """
        return config.DEGREES_PLURAL[self.degree]

    def make_main(self):
        """ Make the main file of LaTeX code. """
        with open(self.PATH_TO_BASE, "r", encoding=self.ENCODING) as base_file:
            main = base_file.read()
        main = main.replace("#PINO", str(self.pino))
        main = main.replace("#DAY", str(self.day))
        main = main.replace("#MONTH", self.month)
        main = main.replace("#YEAR", str(self.year))
        main = main.replace("#GRANTEE", self.grantee)
        main = main.replace("#GENDER", self.gender)
        main = main.replace("#TITLE", self.title)
        main = main.replace("#SUBSIDIARY_TITLES", self.subsidiary_titles)
        main = main.replace("#WHEREAS", self.whereas)
        main = main.replace("#PRONOUN_NOMINATIVE", self.pronoun_nominative)
        main = main.replace("#PRONOUN_DATIVE", self.pronoun_dative)
        main = main.replace("#PRONOUN_POSSESSIVE", self.pronoun_possessive)
        main = main.replace("#ADVANCE_CLAUSE", self.advance_clause)
        main = main.replace("#TRUSTY_CLAUSE", self.trusty_clause)
        main = main.replace("#STATE_CLAUSE", self.state_clause)
        main = main.replace("#DIGNIFY_CLAUSE", self.dignify_clause)
        main = main.replace("#THIRD_INVOCATION", self.third_invocation)
        main = main.replace("#REMAINDER", self.remainder)
        main = main.replace("#RIGHTS_CLAUSE", self.rights_clause)
        main = main.replace("#DEGREE_CLAUSE", self.degree_clause)
        main = main.replace("#DGR_PLURAL", self.degree_plural)
        with open(self.PATH_TO_MAIN, "w", encoding=self.ENCODING) as main_file:
            main_file.write(main)

####################
# HELPER FUNCTIONS #
####################

def get_subsidiary_titles(inputs):
    """ Builds the subsidiary titles string. """
    result = ""
    if inputs is None:
        return result
    for title in inputs:
        if inputs.index(title) == len(inputs)-2:
            result = result+title+" "
        elif inputs.index(title) == len(inputs)-1:
            result = result+"and "+title+", "
        else:
            result = result+title+", "
    return result
