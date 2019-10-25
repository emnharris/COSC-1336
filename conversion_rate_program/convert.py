attempt = 0
MAX_ATTEMPT = 3

MI_TO_KM = 1.60
GAL_TO_L = 3.90
LB_TO_KG = 0.45
IN_TO_CM = 2.54

MI_MEASURE = 'miles'
GAL_MEASURE = 'gallons'
TEMP_MEASURE = 'degrees'
LB_MEASURE = 'pounds'
INCH_MEASURE = 'inches'

def intro():
    print('\n===== IMPERIAL TO METRIC CONVERSION CALCULATOR =====')
    print('=' * 52)

def validate_neg(value, unit):
    #attempt = 0
    #MAX_ATTEMPT = 3
    while(value < 0 and attempt < MAX_ATTEMPT):
        print('\nSorry, negative values are not accepted.\n')
        print('You have',MAX_ATTEMPT - attempt,'tries left.')
        value = float(input('Try again: '))
        attempt = attempt + 1
    if(value < 0 and attempt >= MAX_ATTEMPT):    #if third try is still invalid, end program
        print('\nDATA INVALID\nGOODBYE')
        valid = False
        return valid, value
    else:
        valid = True
        return valid, value

def validate_temp(value,unit):
    #ttempt = 0
    #MAX_ATTEMPT = 3
    while(value > 1000 and attempt < MAX_ATTEMPT):
        print('\nSorry, values over 1000 are not accepted.\n')
        print('You have',MAX_ATTEMPT - attempt,'tries left.')
        value = float(input('Try again: '))
        attempt = attempt + 1
    if(value > 1000 and attempt >= MAX_ATTEMPT):    #if third try is still invalid, end program
        print('\nDATA INVALID\nGOODBYE')
        valid = False
        return valid, value
    else:
        valid = True
        return valid, value

def run_conversion(imperial, measure):
    if measure == MI_MEASURE:
        metric = imperial * MI_TO_KM
    elif measure == TEMP_MEASURE:
        metric = (imperial - 30) * (5/9)
    elif measure == GAL_MEASURE:
        metric = imperial * GAL_TO_L
    elif measure == LB_MEASURE:
        metric = imperial * LB_TO_KG
    else:
        metric = imperial * IN_TO_CM
    return metric
