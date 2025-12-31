from pathlib import Path
import scipy.io
import pandas as pd
from datetime import datetime, timedelta

# %% File-level docstring
"""
par_loader.py

This script provides utility functions to extract and convert PAR (Photosynthetically Active Radiation)
data from a MATLAB .mat file into a pandas DataFrame with properly formatted datetime objects.

Assumes the MATLAB file contains a struct 'PAR_Tahoe' with:
- 'PAR': a numeric array of radiation values
- 'datenum': MATLAB serial date numbers corresponding to timestamps

Dependencies:
- scipy
- pandas
"""

# %% Function definitions

def load_mat_file(filepath):
    """
    Load a MATLAB .mat file.

    Parameters
    ----------
    filepath : str or Path
        Path to the .mat file to be loaded.

    Returns
    -------
    dict
        Dictionary containing MATLAB variables.
    """
    return scipy.io.loadmat(filepath)


def extract_par_struct(mat_data, struct_name="PAR_Tahoe"):
    """
    Extract the PAR structure from the loaded MATLAB data.

    Parameters
    ----------
    mat_data : dict
        Dictionary loaded from the MATLAB file.
    struct_name : str
        Name of the struct containing PAR data.

    Returns
    -------
    dict
        Dictionary with keys 'PAR' and 'datenum' extracted from the structure.
    """
    struct = mat_data[struct_name][0, 0]
    par_array = struct['PAR'].squeeze()
    datenum_array = struct['datenum'].squeeze()
    return {'PAR': par_array, 'datenum': datenum_array}


def datenum_to_datetime(datenum_array):
    """
    Convert a numpy array of MATLAB datenum values to Python datetime objects.

    MATLAB datenum is defined as:
        days since Jan 0, 0000

    Python's datetime.fromordinal uses:
        days since Jan 1, 0001

    Parameters
    ----------
    datenum_array : array-like of float
        MATLAB datenum values.

    Returns
    -------
    list of datetime
        Corresponding Python datetime objects.
    """
    return [
        datetime.fromordinal(int(dn)) + timedelta(days=dn % 1) - timedelta(days=366)
        for dn in datenum_array
    ]


def create_par_dataframe(par_array, datetime_array):
    """
    Create a pandas DataFrame from PAR values and datetime objects.

    Parameters
    ----------
    par_array : array-like of float
        PAR measurements.
    datetime_array : list of datetime
        Corresponding datetime stamps.

    Returns
    -------
    pandas.DataFrame
        DataFrame with 'datetime' and 'PAR' columns.
    """
    return pd.DataFrame({
        "datetime": datetime_array,
        "PAR": par_array
    })

