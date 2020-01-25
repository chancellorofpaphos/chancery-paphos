### Configures the inputs for a given letters patent.

####################
# UNIVERSAL INPUTS #
####################

# "peerage" indicates a patent granting a peerage or baronetage. "other"
# indicates a miscelleneous type of patent.
patent_type = "peerage"

pino = 482

day = 28
# Write out the month's name in full.
month = "December"
year = 6

#######################
# PEERAGE-ONLY INPUTS #
#######################

# If the letters patent are NOT for a peerage, leave well alone.

grantee = "Natalie Knight"
# Either "male" of "female" - no non-binary nonsense!
gender = "female"
# Either "duke", "marquess", "earl", "viscount", "baron" or "baronet".
degree = "baronet"
title = "Baronetess Knight"
# Use a list type. The order here is the order in which they'll appear on
# the letters patent.
subsidiary_titles = []
# Should begin with "Whereas" and end with a comma.
whereas = ("Whereas the first woman to appear in the archives of my "+
           "Seraglio, who made a sufficiently fleshly appearance therein, "+
           "and who was born on or after the first day of January in the "+
           "year of Our Lord two thousand (which most reckon as marking "+
           "the beginning of the present century) was a young actress "+
           "working under the stage name of Natalie Knight, and whose "+
           "birth name was not known to me at the time these letters were "+
           "drawn up,")
# Enter either a code for a standard remainder, or the custom remainder in
# full, beginning with "and" and ending without punctuation.
remainder = "heirs-general-and-bastards"

#####################
# OTHER-ONLY INPUTS #
#####################

# If the letters patent are NOT of "other" type, leave well alone.

filling = (
    "Whereas it has proved necessary to further refine the definition of "+
  "depucelage within the meaning of Paphian Law,\n\n "+
    "\\hspace{20pt} Now be it enacted by my most excellent Grace as "+
  "follows:\\\\\n\n"+
    "\\hspace{20pt} Firstly, the letters patent {\\hoskeroe Statutum "+
  "Virginitatis } are hereby revoked and repealed.\n\n"+
    "\\hspace{20pt} Secondly, the term {\\hoskeroe Depucelage} is to be "+
  "defined, within the meaning of Paphian law, according to the articles "+
  "attached to these letters.")
