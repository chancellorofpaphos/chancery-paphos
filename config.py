"""
This code defines some configurations for the whole repo.
"""

# Installation stuff.
DEFAULT_NON_PYTHON_PACKAGES = ("texlive-full", "poppler-utils")
DEFAULT_PATH_TO_FONTS_DIR = "fonts"
DEFAULT_PATH_TO_PIP_REQ = "pip_requirements.txt"
DEFAULT_PATH_TO_SYSTEM_TRUETYPE_DIR="/usr/share/fonts/truetype/"

# General stuff.
DEFAULT_ENCODING = "utf-8"
DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF = 1024
DEFAULT_PATH_TO_MAIN = "main.tex"
DEFAULT_PATH_TO_OUTPUT = "out.pdf"
ORDINALS = (
    None, "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
    "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
    "nineteenth", "twentieth", "twenty-first", "twenty-second",
    "twenty-third", "twenty-fourth", "twenty-fifth", "twenty-sixth",
    "twenty-seventh", "twenty-eighth", "twenty-ninth", "thirtieth"
)

# Peerage stuff.
ADVANCE_CLAUSES = {
    "peer": "advance, create and prefer",
    "baronet": "erect, appoint and create"
}
TRUSTY_CLAUSES = {
    "duke": "right trusty and right entirely beloved cousin",
    "marquess": "right trusty and entirely beloved cousin",
    "earl": "right trusty and entirely beloved cousin",
    "viscount": "right trusty and well beloved cousin",
    "baron": "trusty and well beloved"
}
STATE_CLAUSES = {
    "peer": "state, degree, style, dignity, title and honour",
    "baronet": "dignity, state and degree"
}
DIGNIFY_CLAUSES = {
    "duke": (
        "and by these presents do dignify, invest and ennoble him by girding "+
        "him with a sword and putting a cap of honour and a coronet of gold "+
        "on his head, and by giving into his hand a rod of gold,"
    ),
    "marquess": (
        "and by these presents do dignify, invest and ennoble him by girding "+
        "him with a sword and putting a cap of honour and a coronet of gold "+
        "on his head, and by giving into his hand a rod of gold,"
    ),
    "earl": (
        "and by these presents do dignify, invest and ennoble him by girding "+
        "him with a sword and putting a cap of honour and a coronet of gold "+
        "on his head,"
    ),
    "female": (
        "and by these presents do dignify, invest and really ennoble her with "+
        "such name, state, degree, title and honour of "
    )
}
NAME_CLAUSES = {
    "duke": "the said name, state, degree, style, dignity, title and honour of",
    "marquess": (
        "the said name, state, degree, style, dignity, title and honour of"
    ),
    "earl": "the said name, degree, style, dignity, title and honour of"
}
PRONOUNS_NOMINATIVE = {
    "male": "he",
    "female": "she"
}
PRONOUNS_DATIVE = {
    "male": "him",
    "female": "her"
}
PRONOUNS_POSSESSIVE = {
    "male": "his",
    "female": "her"
}
RIGHTS_CLAUSES = {
    "peer": "rights, privileges, pre-eminences, immunities and advantages",
    "baronet": "rights, privileges, precedences and advantages"
}
DEGREE_CLAUSES = {
    "duke": "a duke",
    "marquess": "a marquess",
    "earl": "an earl",
    "viscount": "a viscount",
    "baron": "a baron",
    "baronet": "a baronet"
}
DEGREES_PLURAL = {
    "duke": "dukes",
    "marquess": "marquesses",
    "earl": "earls",
    "viscount": "viscounts",
    "baron": "barons",
    "baronet": "baronets"
}
STANDARD_REMAINDERS = {
    "heirs-male": (
        "and the heirs male of #POSSESSIVE body, lawfully begotten and to be "+
        "begotten"
    ),
    "heirs-female": (
        "and the heirs female of #POSSESSIVE body, lawfully begotten and to "+
        "be begotten"
    ),
    "heirs-general": (
        "and the heirs of #POSSESSIVE body, lawfully begotten and to be "+
        "begotten"
    ),
    "heirs-male-and-bastards": "and the heirs male of #POSSESSIVE body",
    "heirs-female-and-bastards": "and the heirs female of #POSSESSIVE body",
    "heirs-general-and-bastards": "and the heirs of #POSSESSIVE body",
    "perpetual": (
        "and #POSSESSIVE heirs whatsoever, or, on the failure of such an "+
        "heir to present himself to me, my heirs and successors, within one "+
        "year of his inheritance, to whomsoever I, my heirs and successors, "+
        "shall choose, and his heirs in like fashion, so that the title may "+
        "have perpetual succession"
    ),
    "life": "for #POSSESSIVE life"
}
