# licencia

# ==============================================================================
# DOCS
# ==============================================================================

"""Linsis test suite."""


# ==============================================================================
# IMPORTS
# ==============================================================================

import os
import pathlib

import pytest

from Linsis import Spectrum


# ==============================================================================
# CONSTANTS
# ==============================================================================


PATH = os.path.abspath(os.path.dirname(__file__))

TEST_PATH = pathlib.Path(PATH) / "test_data"


# ==============================================================================
# FIXTURES
# ==============================================================================

@pytest.fixture(scope="session")
def spectrum160209():
    path = TEST_PATH / "nqgem-s-160209-4542.fits"
    spect = Spectrum(path, 0)
    return spect


# ==============================================================================
# TESTS
# ==============================================================================

def test_match(spectrum160209):
    spectrum = spectrum160209
    assert spectrum.spectral_axis.shape == spectrum.flux.shape


def test_header(spectrum160209):
    spectrum = spectrum160209
    assert isinstance(spectrum.header['EXPTIME'], (float, int))
    assert spectrum.header['EXPTIME'] >= 0.


def test_wav_axis(spectrum160209):
    spectrum = spectrum160209
    assert spectrum.header['CD1_1'] >= 0.
    assert spectrum.header['CTYPE1'] == 'LINEAR'
