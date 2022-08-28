"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "other"

pino = 503

# Date stuff.
day = 30
month = "Quintilis" # Write out the month's name in full.
year = 9

addenda = None # A tuple of PDFs to be stapled onto the end.

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "James Michaels Esquire"
gender = "male" # Either "male" of "female" - no non-binary nonsense!
degree = "baronet" # Either "duke", "marquess", etc.
title = "Baronet Michaels"
subsidiary_titles = None # Use a tuple type.
# The "whereas" should begin with "Whereas" and end with a comma.
whereas = "Whereas my James Michaels Esquire has achieved the milestone of penetrating twenty-one willing and nubile females on camera,"
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-male-and-bastards"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Whereas it has proved necessary to define whom I recognise as holding a given nationality,\n\n"+
    "Now be it enacted as follows:\n\n"+
    "For the purposes of Paphian law, I recognise a person P as holding the nationality of a sovereign state S if:\n\n"+
    "P has ever held, or has ever have been eligible to claim according to the laws of S, citizenship of S; or,\n\n"+
    "Any parent or grandparent of P has ever held, or has ever have been eligible to claim according to the laws of S, citizenship of S; or,\n\n"+
    "Before S came into existence, P lived within what is now the sovereign territory of S for at least ten years."
)
