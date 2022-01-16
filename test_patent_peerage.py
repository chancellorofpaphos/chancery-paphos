"""
This code tests the PatentPeerage class.
"""

# Standard imports.
import os

# Local imports.
import config
from patent_peerage import PatentPeerage

###########
# TESTING #
###########

def test_vicedukedom(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/viceduke.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the creation of letters patent granting a vicedukedom. """
    patent_obj = \
        PatentPeerage(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            grantee="Joseph Bloggs",
            gender="male",
            degree="duke",
            title="Viceduke Bloggs of Paphos",
            subsidiary_titles=("Marquess Bloggs", "Viscount Bloggs"),
            whereas="Whereas my Joseph Bloggs is a good egg,",
            remainder="heirs-male"
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

def test_marquessate(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/marquess.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the creation of letters patent granting a marquessate. """
    patent_obj = \
        PatentPeerage(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            grantee="Joseph Bloggs",
            gender="male",
            degree="marquess",
            title="Marquess Bloggs",
            subsidiary_titles=("Viscount Bloggs",),
            whereas="Whereas my Joseph Bloggs is a good egg,",
            remainder="heirs-male-and-bastards"
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

def test_earldom(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/earl.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the creation of letters patent granting a earldom. """
    patent_obj = \
        PatentPeerage(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            grantee="Joseph Bloggs",
            gender="male",
            degree="earl",
            title="Earl Bloggs",
            whereas="Whereas my Joseph Bloggs is a good egg,",
            remainder="heirs-female"
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

def test_viscountcy(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/viscount.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the creation of letters patent granting a viscountcy. """
    patent_obj = \
        PatentPeerage(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            grantee="Joseph Bloggs",
            gender="male",
            degree="viscount",
            title="Viscount Bloggs",
            whereas="Whereas my Joseph Bloggs is a good egg,",
            remainder="heirs-general"
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

def test_barony(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/baron.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the creation of letters patent granting a barony. """
    patent_obj = \
        PatentPeerage(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            grantee="Joseph Bloggs",
            gender="male",
            degree="baron",
            title="Baron of Somewhere",
            whereas="Whereas my Joseph Bloggs is a good egg,",
            remainder="perpetual"
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

def test_baronetcy(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/baronet.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the creation of letters patent granting a baronetcy. """
    patent_obj = \
        PatentPeerage(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            grantee="Joseph Bloggs",
            gender="male",
            degree="baronet",
            title="Baronet Bloggs",
            whereas="Whereas my Joseph Bloggs is a good egg,",
            remainder="heirs-male"
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)

def test_female(
        path_to_output=config.DEFAULT_PATH_TO_OUTPUT,
        path_to_expected="expected_output/marchioness.pdf",
        max_acceptable_bytes_diff=config.DEFAULT_MAX_ACCEPTABLE_BYTES_DIFF
    ):
    """ Test the creation of letters patent granting a marquessate to a
    woman. """
    patent_obj = \
        PatentPeerage(
            pino=0,
            day=1,
            month="Primilis",
            year=1,
            grantee="Josephine Bloggs",
            gender="female",
            degree="marquess",
            title="Marchioness Bloggs",
            subsidiary_titles=("Viscountess Bloggs",),
            whereas="Whereas my Josephine Bloggs is a good egg,",
            remainder="heirs-male"
        )
    patent_obj.build()
    assert os.path.exists(path_to_output)
    bytes_diff = abs(
        os.path.getsize(path_to_output)-os.path.getsize(path_to_expected)
    )
    assert bytes_diff <= max_acceptable_bytes_diff
    os.remove(path_to_output)
