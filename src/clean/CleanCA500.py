import logging
import src.config as cfg  # config module needs to be run for setting up the logging
from src.utils import utils
import os
import luigi
from luigi import Task, DictParameter, ListParameter, Parameter
import pandas as pd
from pyprojroot import here

logger = logging.getLogger(__name__)

config = luigi.configuration.get_config()
config.read(os.path.join(here(), "config/clean.cfg"))


class CleanCA500(Task):
    """ 
    Transforming the csv file to a parquet file.
    Applying two simple cleaning concepts to the file as an example.

    Args:None

    Return: Saves the parquet file in "data/clean" folder.
    """
    params = DictParameter()
    columns_to_keep = ListParameter()
    output_file_name = Parameter()
    def output(self):
        # create the output path if it does not exit
        cleaned_output = os.path.join(here(), self.params["output"])
        utils.check_directory(cleaned_output)

    def run(self):
        task_input = os.path.join(here(), self.params["input"])
        df = pd.read_csv(task_input, usecols=self.columns_to_keep)
        # lower case all column names and replace any non alphabetical character with underscore        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace("[^A-Za-z0-9]+", "_", regex=True).str.strip(
            "_"
        )
        # save the parquet file
        df.to_parquet(
            os.path.join(here(), self.params["output"], self.output_file_name),
            engine="fastparquet",
        )
        return logger.info("Transform task is finished!")


if __name__ == "__main__":
    luigi.run(["CleanCA500", "--local-scheduler"])
