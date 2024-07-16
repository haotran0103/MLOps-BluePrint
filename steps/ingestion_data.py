import logging

import pandas as pd
from zenml import step

class IngestionData:
    """
    This class is responsible for ingesting data from a specified CSV file.

    Attributes:
    data_path (str): The path to the CSV file to be ingested.

    Methods:
    get_data(): Reads the CSV file and returns the data as a pandas DataFrame.
    """

    def __init__(self, data_path: str):
        """
        Initializes the IngestionData class with the provided data path.

        Parameters:
        data_path (str): The path to the CSV file to be ingested.
        """
        self.data_path = data_path

    def get_data(self) -> pd.DataFrame:
        """
        Reads the CSV file located at the specified data path and returns the data as a pandas DataFrame.

        Returns:
        pd.DataFrame: The data read from the CSV file.
        """
        logging.info(f"Ingesting data from {self.data_path}")
        df = pd.read_csv(self.data_path)
        return df

@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """
    This function ingests data from a specified CSV file using the IngestionData class.

    Parameters:
    data_path (str): The path to the CSV file to be ingested. This parameter is required and must be a string.

    Returns:
    pd.DataFrame: The function returns a pandas DataFrame containing the data read from the CSV file.
    """

    ingestion_data = IngestionData(data_path)
    return ingestion_data.get_data()