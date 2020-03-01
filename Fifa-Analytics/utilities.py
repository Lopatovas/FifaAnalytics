import const

def lbsToKg(lbs):
    try:
        return round(int(lbs[0:-3]) * const.LBS_TO_KG_RATIO)
    except:
        return 0

def fixPrice(price):
    if(price[-1] == 'M'):
        return float(price[1:-1]) * 1000000
    if(price[-1] == 'K'):
        return float(price[1:-1]) * 1000
    return 0

