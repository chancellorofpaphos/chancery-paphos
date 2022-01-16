"""
This code builds a PDF containing a given letters patent.
"""

# Local imports.
import inputs
from patent_other import PatentOther
from patent_peerage import PatentPeerage
from pdf_utilities import make_pdf

#############
# FUNCTIONS #
#############

def make_peerage_patent_obj():
    """ Make an object modelling a patent granting a peerage. """
    result = PatentPeerage()
    attributes_to_set = (
        "pino",
        "day",
        "month",
        "year",
        "grantee",
        "gender",
        "degree",
        "title",
        "subsidiary_titles",
        "whereas",
        "remainder"
    )
    for attribute_name in attributes_to_set:
        attribute_value = getattr(inputs, attribute_name)
        setattr(result, attribute_name, attribute_value)
    return result

def make_other_patent_obj():
    """ Make an object modelling a patent granting a peerage. """
    result = PatentOther()
    attributes_to_set = (
        "pino",
        "day",
        "month",
        "year",
        "filling"
    )
    for attribute_name in attributes_to_set:
        attribute_value = getattr(inputs, attribute_name)
        setattr(result, attribute_name, attribute_value)
    return result

def make_main():
    """ Build the main file of LaTeX code."""
    if inputs.patent_type == "peerage":
        patent_obj = make_peerage_patent_obj()
    else:
        patent_obj = make_other_patent_obj()
    patent_obj.build()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    make_main()
    make_pdf()

if __name__ == "__main__":
    run()
