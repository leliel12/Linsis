# licencia

# ==============================================================================
# DOCS
# ==============================================================================

"""Linsis test suite."""


# ==============================================================================
# IMPORTS
# ==============================================================================

import numpy as np
from astropy.io import fits

import specutils as su

from astropy import units as u


# ==============================================================================
# CLASSES
# ==============================================================================

class Spectrum(su.Spectrum1D):

    def __init__(
        self, spectrum, datastorage, flux_unit=None,
        wav_unit=None, wcs=None, velocity_convention=None, rest_value=None,
        redshift=None, radial_velocity=None, bin_specification=None,
        uncertainty=None, mask=None, meta=None
    ):

        self.spectrum = fits.open(spectrum)
        self.datos = self.spectrum[datastorage].data
        self.header = fits.getheader(spectrum)

        # se construye el objeto tipo Spectrum1D
        spectral_axis = (
            self.header['CRVAL1'] +
            self.header['CD1_1'] * np.arange(0, len(self.datos))) * u.AA

        super().__init__(
            flux=self.datos * u.adu,
            spectral_axis=spectral_axis, wcs=wcs,
            velocity_convention=velocity_convention, rest_value=rest_value,
            redshift=redshift, radial_velocity=radial_velocity,
            bin_specification=bin_specification, uncertainty=uncertainty,
            mask=mask, meta=meta)
