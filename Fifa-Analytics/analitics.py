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
import csv
import graphics

def readData(dataFile, names):
    data = pd.read_csv(dataFile, names=names, encoding='latin-1')
    return data

def getTotalNumberOfData(data):
    return len(data.index)

def getAtributeNumberOfData(data, atributeName):
    return data.count()[atributeName]

def countCardinality(data, atributeName):
    return data[[atributeName]].apply(pd.Series.nunique)[atributeName]

def findMinValue(data, atributeName):
    return data[[atributeName]].apply(pd.Series.min)[atributeName]

def findMaxValue(data, atributeName):
    return data[[atributeName]].apply(pd.Series.max)[atributeName]

def findAvg(data, atributeName):
    return round(data[atributeName].mean())

def findFirstQuant(data, atributeName):
    return round(data[[atributeName]].quantile(.25), config.ROUND_PRESICION)[atributeName]

def findThirdQuant(data, atributeName):
    return round(data[[atributeName]].quantile(.75), config.ROUND_PRESICION)[atributeName]

def findMedian(data, atributeName):
    return round(data[[atributeName]].apply(pd.Series.median), config.ROUND_PRESICION)[atributeName]

def findStandartDeviation(data, atributeName):
    return round(data[[atributeName]].apply(pd.Series.std), config.ROUND_PRESICION)[atributeName]

def modeUtility(value):
    return (value.value_counts().index, value.value_counts())

def findMode(data, atributeName, modeOrder):
    modes = data[[atributeName]].agg(lambda x: modeUtility(x))[atributeName]
    modesList = []
    counter = 0
    nthMaxValue = -1
    maxValue = 99999
    for count in modes[1]:
        if(modeOrder == nthMaxValue):
            if(count == maxValue):
                modesList.append(modes[0][counter])
                counter = counter + 1
            else:
                break
        else:
            if(count < maxValue):
                nthMaxValue = nthMaxValue + 1
                maxValue = count
                if(modeOrder == nthMaxValue):
                    modesList.append(modes[0][counter])
            counter = counter + 1
    final = dict()
    final['names'] = modesList
    final['frequency'] = maxValue
    return final



def constructTableCategory(data, atributeName):
    totalCount = getTotalNumberOfData(data)
    atributesNumberCount = getAtributeNumberOfData(data, atributeName)
    missingValues = str(round((1 - atributesNumberCount/totalCount) * 100, config.ROUND_PRESICION))+'%'
    cardinality = countCardinality(data, atributeName)
    firstMode = findMode(data, atributeName, 0)
    secondMode = findMode(data, atributeName, 1)
    firstModePercentage = str(round((firstMode['frequency']*len(firstMode['names'])/totalCount) * 100, config.ROUND_PRESICION))+'%'
    secondModePercentage = str(round((secondMode['frequency']*len(secondMode['names'])/totalCount) * 100, config.ROUND_PRESICION))+'%'
    # firstModePercentage = str(round((firstMode['frequency']/totalCount) * 100, config.ROUND_PRESICION))+'%'
    # secondModePercentage = str(round((secondMode['frequency']/totalCount) * 100, config.ROUND_PRESICION))+'%'
    return [atributeName, totalCount, missingValues, cardinality, firstMode['names'], firstMode['frequency'], firstModePercentage, secondMode['names'], secondMode['frequency'], secondModePercentage]

def constructTableContinues(data, atributeName):
    totalCount = getTotalNumberOfData(data)
    missingValues = str(round((1 - getAtributeNumberOfData(data, atributeName)/totalCount) * 100, config.ROUND_PRESICION))+'%'
    cardinality = countCardinality(data, atributeName)
    minValue = findMinValue(data, atributeName)
    maxValue = findMaxValue(data, atributeName)
    firstQuant = findFirstQuant(data, atributeName)
    thirdQuant = findThirdQuant(data, atributeName)
    avgValue = findAvg(data, atributeName)
    median = findMedian(data, atributeName)
    standartDeviation = findStandartDeviation(data, atributeName)
    return [atributeName, totalCount, missingValues, cardinality, minValue, maxValue,firstQuant,thirdQuant,avgValue, median, standartDeviation]

def isContinues(data, atributeName):
    try:
        float(data[atributeName][0])
        return True
    except:
        return False

def printTable(data, header, fileName):
    with open(fileName, mode='w') as result_file:
        result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow(header)
        for row in data:
            appendableRow = []
            for item in row:
                appendableRow.append(str(item))
            result_writer.writerow(appendableRow)

def createTables(data):
    continuosTable = []
    categoricalTable = []
    for row in data:
        if(isContinues(data, row)):
            continuosTable.append(constructTableContinues(data, row))
        else:
            categoricalTable.append(constructTableCategory(data, row))
    return [continuosTable, categoricalTable]
    

def driver():
    data = readData(config.FILE_PATH, const.DATA_FIELDS)
    tables = createTables(data)
    printTable(tables[0], const.CONTINOUS_TABLE_HEADER, 'continousTable.csv')
    printTable(tables[1], const.CATEGORY_TABLE_HEADER, 'categoricalTable.csv')
    graphics.paintHistogramContinous(data)
    graphics.paintHistogramCategorical(data)

driver()