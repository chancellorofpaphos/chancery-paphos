"""
This code builds a PDF containing a given letters patent.
"""

# Standard imports.
import os

# Local imports.
import inputs
from patent_peerage import PatentPeerage
from patent_other import PatentOther

#############
# FUNCTIONS #
#############

def make_main():
    """ Builds main.tex."""
    if inputs.patent_type == "peerage":
        make_main_peerage()
    else:
        make_main_other()

def make_main_peerage():
    """ Continues make_main() for the grant of a peerage or baronetage. """
    patent = PatentPeerage(inputs.pino, inputs.day, inputs.month,
                           inputs.year, inputs.grantee, inputs.gender,
                           inputs.degree, inputs.title,
                           inputs.subsidiary_titles, inputs.whereas,
                           inputs.remainder)
    with open("base_peerage.tex", "r") as base_file:
        main = base_file.read()
    main = main.replace("#PINO", str(patent.pino))
    main = main.replace("#DAY", str(patent.day))
    main = main.replace("#MONTH", patent.month)
    main = main.replace("#YEAR", str(patent.year))
    main = main.replace("#GRANTEE", patent.grantee)
    main = main.replace("#GENDER", patent.gender)
    main = main.replace("#TITLE", patent.title)
    main = main.replace("#SUBSIDIARY_TITLES", patent.subsidiary_titles)
    main = main.replace("#WHEREAS", patent.whereas)
    main = main.replace("#PRONOUN_NOMINATIVE", patent.pronoun_nominative)
    main = main.replace("#PRONOUN_DATIVE", patent.pronoun_dative)
    main = main.replace("#PRONOUN_POSSESSIVE", patent.pronoun_possessive)
    main = main.replace("#ADVANCE_CLAUSE", patent.advance_clause)
    main = main.replace("#TRUSTY_CLAUSE", patent.trusty_clause)
    main = main.replace("#STATE_CLAUSE", patent.state_clause)
    main = main.replace("#DIGNIFY_CLAUSE", patent.dignify_clause)
    main = main.replace("#THIRD_INVOCATION", patent.third_invocation)
    main = main.replace("#REMAINDER", patent.remainder)
    main = main.replace("#RIGHTS_CLAUSE", patent.rights_clause)
    main = main.replace("#DEGREE_CLAUSE", patent.degree_clause)
    main = main.replace("#DGR_PLURAL", patent.degree_plural)
    with open("main.tex", "w") as main_file:
        main_file.write(main)

def make_main_other():
    """ Continues make_main() for letters patent of "other" type. """
    patent = PatentOther(inputs.pino, inputs.day, inputs.month,
                         inputs.year, inputs.filling)
    with open("base_other.tex", "r") as base_file:
        main = base_file.read()
    main = main.replace("#PINO", str(patent.pino))
    main = main.replace("#DAY", str(patent.day))
    main = main.replace("#MONTH", patent.month)
    main = main.replace("#YEAR", str(patent.year))
    main = main.replace("#FILLING", patent.filling)
    with open("main.tex", "w") as main_file:
        main_file.write(main)

def make_pdf():
    """ Ronseal. """
    os.system("xelatex main.tex")
    os.system("cp main.pdf out.pdf")
    os.system("rm main.aux main.log main.pdf main.tex")

###################
# RUN AND WRAP UP #
###################

def run():
    make_main()
    make_pdf()

if __name__ == "__main__":
    run()
