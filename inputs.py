"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "other"

pino = 487

day = 6
# Write out the month's name in full.
month = "Sextilis"
year = 7

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "Luke Babur Khan"
# Either "male" of "female" - no non-binary nonsense!
gender = "male"
# Either "duke", "marquess", "earl", "viscount", "baron" or "baronet".
degree = "baronet"
title = "Baronet Babur"
# Use a list type. The order here is the order in which they'll appear on
# the letters patent.
subsidiary_titles = []
# Should begin with "Whereas" and end with a comma.
whereas = ("Whereas my Luke Babur Khan has achieved the feat of "+
           "penetrating twenty-one willing and nubile girls on camera,")
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-general-and-bastards"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Whereas, on the first day of Duodecember in the fourth year of my "+
    "regency in the Kingdom of Cyprus, I issued letters patent convicting "+
    "one Cara Horgan of treachery,\n\n"
    "Now let all know that I, in consideration of circumstances "+
    "represented to me with due humility, am pleased to extend my mercy "+
    "to the said { \\hoskeroe Cara Horgan } and to remit and "+
    "{ \\hoskeroe Pardon } all such pains and forfeitures resulting "+
    "from the aforesaid conviction.")
