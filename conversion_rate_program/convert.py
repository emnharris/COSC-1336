def intro():
    print('\n===== IMPERIAL TO METRIC CONVERSION CALCULATOR =====')
    print('=' * 52)

def validate_neg(value, unit):
    attempt = 0
    max_attempt = 3
    while(value < 0 and attempt < max_attempt):
        print('\nSorry, negative values are not accepted.\n')
        print('You have',max_attempt - attempt,'tries left.')
        value = float(input('Try again: '))
        attempt = attempt + 1
    if(value < 0 and attempt >= max_attempt):    #if third try is still invalid, end program
        print('\nDATA INVALID\nGOODBYE')
        valid = False
        return valid, value
    else:
        valid = True
        return valid, value

def validate_temp(value,unit):
    attempt = 0
    max_attempt = 3
    while(value > 1000 and attempt < max_attempt):
        print('\nSorry, values over 1000 are not accepted.\n')
        print('You have',max_attempt - attempt,'tries left.')
        value = float(input('Try again: '))
        attempt = attempt + 1
    if(value > 1000 and attempt >= max_attempt):    #if third try is still invalid, end program
        print('\nDATA INVALID\nGOODBYE')
        valid = False
        return valid, value
    else:
        valid = True
        return valid, value

def run_conversion(imperial, measure):
    mi_to_km = 1.60
    gal_to_L = 3.90
    lb_to_kg = 0.45
    in_to_cm = 2.54

    MI_MEASURE = 'miles'
    GAL_MEASURE = 'gallons'
    TEMP_MEASURE = 'degrees'
    LB_MEASURE = 'pounds'
    INCH_MEASURE = 'inches'

    if measure == MI_MEASURE:
        metric = imperial * mi_to_km
    elif measure == TEMP_MEASURE:
        metric = (imperial - 30) * (5/9)
    elif measure == GAL_MEASURE:
        metric = imperial * gal_to_L
    elif measure == LB_MEASURE:
        metric = imperial * lb_to_kg
    else:
        metric = imperial * in_to_cm
    return metric
