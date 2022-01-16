"""
Configures the inputs for a given letters patent.
"""

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "peerage"

pino = 502

# Date stuff.
day = 13
month = "Unodecember" # Write out the month's name in full.
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
whereas = "Whereas my James Michaels Esquire has achieved the milestone of penetrating twenty-one willing and nubile females on camera,"
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-male-and-bastards"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Whereas I issued letters patent on the tenth day of November in the fourth year of my regency in the Kingdom of Cyprus known as { \hoskeroe Gravitas Iniquitatis } concerning the seriousness of various crimes,\n\n"
    "Now be it enacted as follows:\n\n"
    "The letters patent known as { \hoskeroe Gravitas Iniquitatis } are hereby revoked and repealed.\n\n"
    "Crimes shall be classified as Class A, Class B or Class C, with Class A being the most serious and Class C being the least serious.\n\n"
    "Any violation of { \hoskeroe Statutum Censurae } involving either blasphemy or feminism, as these terms are defined within said statute, is a Class A offence; any violation of the same statute falling within the definition of less serious kinds of sexual perversion is a Class C offence. Any violation of { \hoskeroe Statutum Coculae } is considered a Class A offence. Any other violation of statute law is a Class B offence, unless the statute in question contains a provision to the contrary.\n\n"
    "Classification of offences against common law shall be done on a case by case basis. However, the following offences are Class A offences in the absence of exceptional mitigating circumstances: aggravated assault, arson, extortion, fraud, grand larceny, murder, perjury, rape, and treason."
)
