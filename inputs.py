"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "peerage"

pino = 501

# Date stuff.
day = 24
month = "October" # Write out the month's name in full.
year = 8

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "James Michaels Esquire"
gender = "male" # Either "male" of "female" - no non-binary nonsense!
degree = "baronet" # Either "duke", "marquess", etc.
title = "Baronet Michaels"
subsidiary_titles = [] # Use a list type.
# The "whereas" should begin with "Whereas" and end with a comma.
whereas = ("Whereas my James Michaels Esquire has achieved the milestone of penetrating twenty-one willing and nubile females on camera,")
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-male-and-bastards"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Be it enacted as follows:\n\n"+
    "The articles attached to these presents are hereby confirmed as the essential { \\hoskeroe Doctrine of the Religion of Paphos } which is the state ritual of this my Duchy of Paphos.")
