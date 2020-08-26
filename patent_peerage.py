"""
This code holds a class which models the letters patent pertaining to a
given peerage.
"""

# Local imports.
import constants
from patent_other import get_ordinal

##############
# MAIN CLASS #
##############

class PatentPeerage:
    """ The class in question. """
    def __init__(self, pino, day, month, year, grantee, gender, degree,
                 title, subsidiary_titles, whereas, remainder):
        self.pino = pino
        self.day = get_ordinal(day)
        self.month = month
        self.year = get_ordinal(year)
        self.grantee = grantee
        self.gender = gender
        self.degree = degree
        self.title = title
        self.subsidiary_titles = get_subsidiary_titles(subsidiary_titles)
        self.whereas = whereas
        self.pronoun_nominative = self.get_pronoun_nominative()
        self.pronoun_dative = self.get_pronoun_dative()
        self.pronoun_possessive = self.get_pronoun_possessive()
        self.advance_clause = self.get_advance_clause()
        self.trusty_clause = self.get_trusty_clause()
        self.state_clause = self.get_state_clause()
        self.dignify_clause = self.get_dignify_clause()
        self.third_invocation = self.get_third_invocation()
        self.remainder = self.get_remainder(remainder)
        self.rights_clause = self.get_rights_clause()
        self.degree_clause = self.get_degree_clause()
        self.degree_plural = self.get_degree_plural()

    def get_pronoun_nominative(self):
        """ Looks up the result in constants.py. """
        return constants.pronouns_nominative[self.gender]

    def get_pronoun_dative(self):
        """ Looks up the result in constants.py. """
        return constants.pronouns_dative[self.gender]

    def get_pronoun_possessive(self):
        """ Looks up the result in constants.py. """
        return constants.pronouns_possessive[self.gender]

    def get_advance_clause(self):
        """ Looks up the result in constants.py. """
        if self.degree == "baronet":
            return constants.advance_clauses["baronet"]
        return constants.advance_clauses["peer"]

    def get_trusty_clause(self):
        """ Looks up the result in constants.py. """
        if self.degree == "baronet":
            return ""
        return constants.trusty_clauses[self.degree]

    def get_state_clause(self):
        """ Looks up the result in constants.py. """
        if self.degree == "baronet":
            return constants.state_clauses["baronet"]
        return constants.state_clauses["peer"]

    def get_dignify_clause(self):
        """ Looks up the result in constants.py. """
        if ((self.degree == "duke") or (self.degree == "marquess") or
                (self.degree == "earl")):
            if self.gender == "female":
                result = constants.dignify_clauses["female"]+self.title+", "
            else:
                result = constants.dignify_clauses[self.degree]
            return result
        else:
            return ""

    def get_third_invocation(self):
        """ Constructs the third invocation of the title granted. """
        if ((self.degree == "duke") or (self.degree == "marquess")):
            result = ("the said name, state, degree, style, dignity, "+
                      "tile and honour of "+self.title)
        elif self.degree == "earl":
            result = ("the said name, degree, style, dignity, title and "+
                      "honour of "+self.title)
        else:
            result = ""
        return result

    def get_remainder(self, remainder):
        """ Looks up the result in constants.py, or not. """
        if remainder in constants.standard_remainders.keys():
            result = constants.standard_remainders[remainder]
        else:
            result = remainder
        result = result.replace("#POSSESSIVE", self.pronoun_possessive)
        return result

    def get_rights_clause(self):
        """ Looks up the result in constants.py. """
        if self.degree == "baronet":
            return constants.rights_clauses["baronet"]
        return constants.rights_clauses["peer"]

    def get_degree_clause(self):
        """ Looks up the result in constants.py. """
        return constants.degree_clauses[self.degree]

    def get_degree_plural(self):
        """ Looks up the result in constants.py. """
        return constants.degrees_plural[self.degree]

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
