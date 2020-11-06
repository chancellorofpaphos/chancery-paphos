"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "peerage"

pino = 488

day = 19
# Write out the month's name in full.
month = "October"
year = 7

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "Stephanie Ahthion"
# Either "male" of "female" - no non-binary nonsense!
gender = "female"
# Either "duke", "marquess", "earl", "viscount", "baron" or "baronet".
degree = "baronet"
title = "Petty Princess Seychelloise"
# Use a list type. The order here is the order in which they'll appear on
# the letters patent.
subsidiary_titles = []
# Should begin with "Whereas" and end with a comma.
whereas = ("Whereas I have corresponded with one Stephanie Ahthion, "+
           "commonly known as Yannicka Love, of the Republic of the "+
           "Seychelles, and whereas she has helped me to establish an "+
           "honorary consulate in that country,")
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-female-and-bastards"

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
