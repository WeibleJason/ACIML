# Algorithm from 'A Course in Machine Learning' - Hal Daume
import pandas as pd
import numpy as np
from collections import Counter

class Node:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def PrintTree(self):
        print(self.data)

def DecisionTreeTrain(examples, feature_dict):
    examples = np.array(list(examples))
    no_set_index = set()
    yes_set_index = set()
    feature_score_dict = {}
    guess = getMaxKey(feature_dict) # Guess the most frequent answer in data
    
    if(len(feature_dict) == 0): # if label in data are unambiguous then return leaf(guess)
        return Node(guess)
    else: 
        for x in feature_dict:
            i = 0
            while(i < len(x)):
                value = feature_dict.get(x)
                if(value[i] == 'y' or value[i] == '1' or value[i] == '2'):
                    yes_set_index.add(i)
                else:
                    no_set_index.add(i)
                i = i + 1
            score_yes = 0
            j = 0
            for y in yes_set_index:
                feature = None
                if (j < len(feature_dict.keys())):
                    feature = list(feature_dict.keys())[j]
                    score_yes = list(feature_dict.get(feature)).count(guess)
                j = j + 1
            score_no = 0
            k = 0
            for y in no_set_index:
                feature = None
                if (k < len(feature_dict.keys())):
                    feature = list(feature_dict.keys())[k]
                    score_no = list(feature_dict.get(feature)).count(guess)
                k = k + 1
            feature_score_dict.update({x:score_yes+score_no})
    max_feature = MaxKey(feature_score_dict)
    feature_dict.pop(max_feature)
    no_set_examples = set()
    for x in no_set_index:
        example_list = examples.tolist()
        example_to_add = ()
        if(x < len(example_list)):
            example_to_add = example_list[x]
        no_set_examples.add(tuple(example_to_add))
    yes_set_examples = set()
    for x in yes_set_index:
        example_list = examples.tolist()
        example_to_add = ()
        if(x < len(example_list)):
            example_to_add = example_list[x]
        yes_set_examples.add(tuple(example_to_add))
    left = DecisionTreeTrain(no_set_examples,dict(feature_dict))
    right = DecisionTreeTrain(yes_set_examples,dict(feature_dict))
    return Node(max_feature,left,right)


def getMaxKey(feature_dict):
    max_value = None
    max_value_count = 0
    for x in feature_dict.values():
        occurence_count = Counter(x)
        temp_max_value = occurence_count.most_common(1)[0][0]
        temp_max_value_count = occurence_count.most_common(1)[0][1]
        if(temp_max_value_count > max_value_count):
            max_value = temp_max_value
            max_value_count = temp_max_value_count
    return max_value
    
def MaxKey(feature_dict):
    max_value = 0
    max_key = None
    for x in feature_dict:
        temp_max_value = feature_dict.get(x)
        if (temp_max_value > max_value):
            max_value = temp_max_value
            max_key = x
    return max_key

