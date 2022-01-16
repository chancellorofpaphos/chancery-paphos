"""
This code tests the PatentOther class.
"""

# Standard imports.
import os

# Local imports.
import config
from patent_other import PatentOther

###########
# TESTING #
###########

def test_patent_other(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/other.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the PatentOther class. """
    patent_obj = \
        PatentOther(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            filling="Something silly."
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

def test_addenda(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/with_addenda.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the adding of other documents to the end of the output. """
    patent_obj = \
        PatentOther(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            filling="The UN Charter is a cruel hoax.",
            addenda=("expected_output/un_charter.pdf",)
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

test_addenda()
