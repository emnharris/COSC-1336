# conversion constants
mi_to_km = 1.60
gal_to_L = 3.90
lb_to_kg = 0.45
in_to_cm = 2.54
# max attempt constant
max_attempt = 3

def main():
    intro()
    mi = float(input('Miles: '))
    unit = 'miles'
    valid, mi = validate_neg(mi, unit)
    if valid:
        km = run_conversion(mi, unit)
        print('\n',mi,' miles = ',format(km,',.1f'),' kilometers', sep='')
    if valid:
        degF = float(input('\n\nDegrees F: '))
        unit = 'temperature'
        valid, degF = validate_temp(degF, unit)
        if valid:
            degC = run_conversion(degF, unit)
            print('\n',degF,' degrees F = ',format(degC,',.1f'),' degrees C', sep='')
    if valid:
        gal = float(input('\n\nGallons: '))
        unit = 'gallons'
        valid, gal = validate_neg(gal, unit)
        if valid:
            litr = run_conversion(gal, unit)
            print('\n',gal,' gallons = ',format(litr,',.1f'),' liters', sep='')
    if valid:
        lb = float(input('\n\nDry pounds: '))
        unit = 'pounds'
        valid, lb = validate_neg(lb, unit)
        if valid:
            kg = run_conversion(lb, unit)
            print('\n',lb,' pounds = ',format(kg,',.1f'),' kilograms', sep='')
    if valid:
        inches = float(input('\n\nInches: '))
        unit = 'inches'
        valid, inches = validate_neg(inches, unit)
        if valid:
            cm = run_conversion(inches, unit)
            print('\n',inches,' inches = ',format(cm,',.1f'),' centimenters', sep='')

def intro():
    print('\n===== IMPERIAL TO METRIC CONVERSION CALCULATOR =====')
    print('=' * 52)

def validate_neg(value, unit):
    attempt = 0
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
    if measure == 'miles':
        metric = imperial * mi_to_km
    elif measure == 'temperature':
        metric = (imperial - 30) * (5/9)
    elif measure == 'gallons':
        metric = imperial * gal_to_L
    elif measure == 'pounds':
        metric = imperial * lb_to_kg
    else:
        metric = imperial * in_to_cm
    return metric

main()