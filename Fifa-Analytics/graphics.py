import span as span
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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