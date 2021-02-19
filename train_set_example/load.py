import pandas as pd



def load_csv(relative_path):
    """
    Load the file: relative_path
    :param relative_path
    :returns pandas matrix of data
    """
    data = pd.read_csv(relative_path, sep=',', header=None)
    return data
