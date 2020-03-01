import span as span
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import const

def paintHistogramContinous(data):
    data.describe(include='all')
    data.hist()
    plt.show()

def paintHistogramCategorical(data):
    clubGrouped = data.groupby([const.CLUB]).size()
    clubGrouped.plot(kind='bar')
    plt.show()

    sponsorGrouped = data.groupby([const.SPONSOR]).size()
    sponsorGrouped.plot(kind='bar')
    plt.show()

    footGroup = data.groupby([const.PREFERRED_FOOT]).size()
    footGroup.plot(kind='bar')
    plt.show()

    positionGroup = data.groupby([const.POSITION]).size()
    positionGroup.plot(kind='bar')
    plt.show()

    jerseyGroup = data.groupby([const.JERSEY]).size()
    jerseyGroup.plot(kind='bar')
    plt.show()

    heightGroup = data.groupby([const.HEIGHT]).size()
    heightGroup.plot(kind='bar')
    plt.show()

def paintScatterPlot(data):
    #kinda compatable
    data.plot.scatter(x=const.OVERALL, y=const.WAGE, colormap='viridis')
    data.plot.scatter(x=const.OVERALL, y=const.POTENTIAL, colormap='viridis')
    plt.show()
    #no connection
    data.plot.scatter(x=const.AGE, y=const.OVERALL, colormap='viridis')
    data.plot.scatter(x=const.WEIGHT, y=const.POTENTIAL, colormap='viridis')
    plt.show()

def paintCorrelations(data):
    correlations = data[[const.AGE, const.OVERALL, const.POTENTIAL, const.WAGE, const.VALUE,
           const.WEIGHT]].corr()
    scatter_matrix(correlations,figsize=(12,16), alpha=1)
    plt.show()