import numpy as np
import pandas as pd

def most_frequent(array):
    '''
    returns the a dictionary of the frequency
    :param: list - the list of items
    :returns: a dictionary whose key is the item and whose value is the frequency
    '''
    frequency = 0
    item = None
    max = 0
    data_series = pd.Series(array)
    frequency_series = data_series.value_counts(normalize=True)
    keys = frequency_series.keys()
    frequency_dict = {}
    i = 0
    for x in keys:
        frequency_dict.update({keys[i]: frequency_series[i]})
        i = i + 1


    return frequency_dict


        

    
        
