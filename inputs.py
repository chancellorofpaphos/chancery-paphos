"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "peerage"

pino = 490

# Date stuff.
day = 29
month = "Primilis" # Write out the month's name in full.
year = 8

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "Michelle Anderson"
# Either "male" of "female" - no non-binary nonsense!
gender = "female"
# Either "duke", "marquess", "earl", "viscount", "baron" or "baronet".
degree = "baronet"
title = "Baronet Anderson"
# Use a list type. The order here is the order in which they'll appear on
# the letters patent.
subsidiary_titles = []
# Should begin with "Whereas" and end with a comma.
whereas = ("Whereas the gentlewoman known as Michelle Anderson is the "+
           "first woman added to my Seraglio born on or after the first "+
           "day of January in the year two thousand and one of the "+
           "Gregorian calendar, which many take to be the first day of "+
           "the twenty-first century, ")
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-male-and-bastards"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Whereas my entirely beloved counsellor The Honourable The Chancellor "+
    "of Paphos has humbly submitted the document known as The Statute of "+
    "of San Fernando, which he published on the first day of March two "+
    "thousand and twenty-one in the Gregorian calendar, to my Ducal "+
    "consideration,\n\n"+
    "Now be it enacted as follows:\n\n"+
    "A new body politic, the { \hoskeroe County of San Fernando } by "+
    "name, is hereby created within my Duchy of Paphos.\n\n"+
    "The said document known as The Statute of San Fernando shall "+
    "henceforth have the force of law.")
