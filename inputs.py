"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "other"

pino = 500

# Date stuff.
day = 3
month = "Quartilis" # Write out the month's name in full.
year = 8

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "Jacob Adams, Earl of the Valley"
gender = "male" # Either "male" of "female" - no non-binary nonsense!
degree = "baron" # Either "duke", "marquess", etc.
title = "Baron of Adams"
subsidiary_titles = [] # Use a list type.
# The "whereas" should begin with "Whereas" and end with a comma.
whereas = ("Whereas yesterday I issued letters patent creating the Barony of Adams, and promised to issue further letters patent granting said barony to another,")
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "perpetual"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Be it enacted as follows:\n\n"+
    "The articles attached to these presents are hereby confirmed as the essential { \\hoskeroe Doctrine of the Religion of Paphos } which is the state ritual of this my Duchy of Paphos.")
