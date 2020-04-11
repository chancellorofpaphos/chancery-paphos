"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "other"

pino = 484

day = 1
# Write out the month's name in full.
month = "Primilis"
year = 7

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "John Moore"
# Either "male" of "female" - no non-binary nonsense!
gender = "male"
# Either "duke", "marquess", "earl", "viscount", "baron" or "baronet".
degree = "baronet"
title = "Baronet Moore of Tampa"
# Use a list type. The order here is the order in which they'll appear on
# the letters patent.
subsidiary_titles = []
# Should begin with "Whereas" and end with a comma.
whereas = ("Whereas my James Moore has achieved the feat of penetrating "+
           "twenty-one willing and nubile girls on camera,")
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-general-and-bastards"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Be it enacted by my most excellent Grace, and by the authority of "+
    "the same, that {\\hoskeroe Fionnghuala O'Connor}, commonly known as "+
    "Fionnula Flanagan, of the Republic of Ireland, and {\\hoskeroe "+
    "Stephane Caillard}, commonly known as St\\'ephane Caillard, of the "+
    "French Republic, stand and be {\\hoskeroe Convicted and Attainted } "+
    "of treachery, and that they incur all penalties and forfeitures as "+
    "criminals charged, tried and condemned.")
