"""
This code defines an abstract PATENT class, to be inherited by child classes.
"""

# Standard imports.
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

# Local imports.
from .constants import ORDINALS, CYPRIAN_MONTHS

# Local constants.
WORKING_STEM = "main"
OUTPUT_DIRNAME = "_out"
DEFAULT_PATH_TO_OUTPUT = str(Path(OUTPUT_DIRNAME)/"patent.pdf")
PATH_OBJ_TO_IMAGE_DIR = Path(__file__).parent/"images"
PRE_PARAGRAPH = "    \\hspace{20pt} "

##############
# MAIN CLASS #
##############

@dataclass
class Patent:
    """ The class in question. """
    # Class attributes.
    LATEX_COMMAND: ClassVar[str] = "xelatex"
    WORKING_FN: ClassVar[str] = f"{WORKING_STEM}.tex"
    IMMEDIATE_OUTPUT_FN: ClassVar[str] = f"{WORKING_STEM}.pdf"
    EXTENSIONS_TO_REMOVE: ClassVar[tuple] = (".aux", ".log", ".pdf", ".tex")
    PATH_TO_BASE: ClassVar[str] = str(Path(__file__).parent/"tex"/"base.tex")
    PATH_TO_TOP_IMAGE: ClassVar[str] = \
        str(PATH_OBJ_TO_IMAGE_DIR/"thomas_duke_of.png")
    PATH_TO_SIGNATURE: ClassVar[str] = \
        str(PATH_OBJ_TO_IMAGE_DIR/"signature.png")
    PATH_TO_SEAL: ClassVar[str] = str(PATH_OBJ_TO_IMAGE_DIR/"seal.png")
    TOP_IMAGE_MARKER: ClassVar[str] = "#TOP_IMAGE"
    SIGNATURE_MARKER: ClassVar[str] = "#SIGNATURE"
    SEAL_MARKER: ClassVar[str] = "#SEAL"
    PINO_MARKER: ClassVar[str] = "#PINO"
    DAY_ORDSTR_MARKER: ClassVar[str] = "#DAY_ORDSTR"
    MONTH_STR_MARKER: ClassVar[str] = "#MONTH_STR"
    YEAR_ORDSTR_MARKER: ClassVar[str] = "#YEAR_ORDSTR"
    BODY_MARKER: ClassVar[str] = "#BODY"

    # Object attributes.
    pino: int = None
    day_num: int = None
    day_ordstr: str = None
    month_num: int = None
    month_str: str = None
    year_num: int = None
    year_ordstr: str = None
    body: str = None
    body_paragraphs: list[str] = None
    path_to_output: str = DEFAULT_PATH_TO_OUTPUT
    clean_bool: bool = True

    def __post_init__(self):
        self.update_date_fields()
        if self.pino:
            self.path_to_output = str(Path(OUTPUT_DIRNAME)/f"{self.pino}.pdf")

    def update_date_fields(self):
        """ Set any unset date fields, where possible. """
        if self.day_num and not self.day_ordstr:
            self.day_ordstr = ORDINALS[self.day_num]
        if (self.month_num is not None) and (not self.month_str):
            self.month_str = CYPRIAN_MONTHS[self.month_num]
        if self.year_num and not self.year_ordstr:
            self.year_ordstr = ORDINALS[self.year_num]
        if self.body_paragraphs and not self.body:
            self.body = build_body_from_paragraphs(self.body_paragraphs)

    def get_general_replacement_pairs(self):
        """ Return a tuple of pairs of strings, giving the substrings to be
        replaced and their replacements, for the GENERAL replacements that
        need to be done for every kind of patent. """
        result = (
            (self.TOP_IMAGE_MARKER, self.PATH_TO_TOP_IMAGE),
            (self.SIGNATURE_MARKER, self.PATH_TO_SIGNATURE),
            (self.SEAL_MARKER, self.PATH_TO_SEAL),
            (self.PINO_MARKER, str(self.pino)),
            (self.DAY_ORDSTR_MARKER, self.day_ordstr),
            (self.MONTH_STR_MARKER, self.month_str),
            (self.YEAR_ORDSTR_MARKER, self.year_ordstr)
        )
        return result

    def get_special_replacement_pairs(self):
        """ Return a tuple of pairs of strings, giving the substrings to be
        replaced and their replacements, for the SPECIAL replacements that
        need to be done only for the kind of patent corresponding to this
        inheritance. """
        result = ((self.BODY_MARKER, self.body),)
        return result

    def build_working_tex(self):
        """ Build the working TeX file, which we'll then compile. """
        with open(self.PATH_TO_BASE, "r") as base_file:
            tex_str = base_file.read()
        replacement_pairs = (
            self.get_general_replacement_pairs()+
            self.get_special_replacement_pairs()
        )
        for pair in replacement_pairs:
            tex_str = tex_str.replace(*pair)
        with open(self.WORKING_FN, "w") as working_tex:
            working_tex.write(tex_str)

    def compile_working_tex(self):
        """ Compile the working TeX file. """
        subprocess.run([self.LATEX_COMMAND, self.WORKING_FN], check=True)
        Path(OUTPUT_DIRNAME).mkdir(exist_ok=True)
        shutil.copyfile(self.IMMEDIATE_OUTPUT_FN, self.path_to_output)

    def clean(self):
        """ Clean up any redundant generated files. """
        for extension in self.EXTENSIONS_TO_REMOVE:
            Path(WORKING_STEM+extension).unlink()

    def generate(self):
        """ (1) Build the TeX file. (2) Compile it. (3) Clean (if req). """
        self.build_working_tex()
        self.compile_working_tex()
        if self.clean_bool:
            self.clean()

####################
# HELPER FUNCTIONS #
####################

def build_body_from_paragraphs(paragraphs):
    """ Ronseal. """
    between_paragraphs = "\n\n"+PRE_PARAGRAPH
    result = between_paragraphs.join(paragraphs)
    return result
