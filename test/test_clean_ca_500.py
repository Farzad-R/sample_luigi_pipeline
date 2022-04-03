## Here I am writing to basic test one for checking the file extensions 
# and one for checking the availability of possible Nans in the index
# and we can see that both test can pass!

import configparser
import os
from pyprojroot import here
import json
import unittest
import pandas as pd


config = configparser.RawConfigParser()
config.read(os.path.join(here(), "config/clean.cfg"))
params_str = config.get("CleanCA500", "params")
params_dict = json.loads(params_str)
FILES_LIST = os.listdir(os.path.join(here(), params_dict["output"]))


class MetStationsTest(unittest.TestCase):
    def test_if_all_files_in_directory_are_parquet(self):
        for file in FILES_LIST:
            split_tup = os.path.splitext(file)
            file_extension = split_tup[1]
            self.assertEqual(".parquet", file_extension)

    def test_to_check_there_is_no_NaT_in_index(self):
        for file in FILES_LIST:
            df = pd.read_parquet(os.path.join(here(), params_dict["output"], file))
            full_shape = df.shape[0]
            shape_without_NaT = df.loc[pd.notnull(df.index)].shape[0]
            self.assertEqual(full_shape, shape_without_NaT)
