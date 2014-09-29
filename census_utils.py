import pandas as pd
import os
import re
import h5py
from census import Census
from us import states

acs5_vars_2007to2011 = pd.read_hdf("helpful_census_documentation.hdf5", "acs5_2007to2011_variables")

census_wrapper = Census("324fbab1e08ff17ae4f6e0c1dba2f37683080320")

