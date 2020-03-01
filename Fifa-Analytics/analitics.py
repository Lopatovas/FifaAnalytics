import span as span
import pandas as pd
import numpy as np
import json as json
import collections
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
import const
import config

def readData(dataFile, names):
    data = pd.read_csv(dataFile, names=names)
    return data

def driver():
    data = readData(config.FILE_PATH, const.dataFields)
    print(data)

driver()