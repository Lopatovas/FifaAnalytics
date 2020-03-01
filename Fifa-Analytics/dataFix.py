import math

def removeExtremeData(data, atributeName):
    firstQuant = data[atributeName].quantile(0.25)
    thirdQuant = data[atributeName].quantile(0.75)
    interQuant = thirdQuant-firstQuant
    lower  = firstQuant-1.5*interQuant
    upper = thirdQuant+1.5*interQuant
    fixedData = data.loc[(data[atributeName] > lower) & (data[atributeName] < upper)]
    return fixedData

def addEmptyData(data, atributeName, insertable):
    counter = 0
    for row in data[atributeName]:
        if(isinstance(row, str)):
            counter = counter +1
            continue
        if(math.isnan(row)):
            data[atributeName][counter] = insertable
        counter = counter +1
    return data