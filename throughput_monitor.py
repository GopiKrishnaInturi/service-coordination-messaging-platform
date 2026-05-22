import pandas as pd

def generate_metrics(dataframe: pd.DataFrame):
    return dataframe.describe().to_dict()