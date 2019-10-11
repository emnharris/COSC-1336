# conversion constants
mi_to_km = 1.60
gal_to_L = 3.90
lb_to_kg = 0.45
in_to_cm = 2.54
# max attempt constant
max_attempt = 3
# data validation constant
valid = True

def main():
    intro()
    mi = float(input('Miles: '))
    unit = 'miles'
    validate_neg(mi, unit)
    if valid:
        degF = float(input('\n\nDegrees F: '))
        unit = 'temperature'
        validate_temp(degF, unit)
    if valid:
        gal = float(input('\n\nGallons: '))
        unit = 'gallons'
        validate_neg(gal, unit)
    if valid:
        lb = float(input('\n\nDry pounds: '))
        unit = 'pounds'
        validate_neg(lb, unit)
    if valid:
        inches = float(input('\n\nInches: '))
        unit = 'inches'
        validate_neg(inches, unit)

def intro():
    print('\n===== IMPERIAL TO METRIC CONVERSION CALCULATOR =====')
    print('=' * 52)

def validate_neg(value, unit):
    #attempt constant for limited attempt looping data validation
    attempt = 0
    while(value < 0 and attempt < max_attempt):
        print('\nSorry, negative values are not accepted.\n')
        print('You have',max_attempt - attempt,'tries left.')
        value = float(input('Try again: '))
        attempt = attempt + 1
    if(value < 0 and attempt >= max_attempt):    #if third try is still invalid, end program
        print('\nDATA INVALID\nGOODBYE')
        global valid
        valid = False
    else:
        run_conversion(value, unit)

def validate_temp(value,unit):
    attempt = 0
    while(value > 1000 and attempt < max_attempt):
        print('\nSorry, values over 1000 are not accepted.\n')
        print('You have',max_attempt - attempt,'tries left.')
        value = float(input('Try again: '))
        attempt = attempt + 1
    if(value > 1000 and attempt >= max_attempt):    #if third try is still invalid, end program
        print('\nDATA INVALID\nGOODBYE')
        global valid
        valid = False
    else:
        run_conversion(value, unit)

def run_conversion(imperial, measure):
    if measure == 'miles':
        km = imperial * mi_to_km
        print('\n',imperial,' miles = ',format(km,',.1f'),' kilometers', sep='')
    elif measure == 'temperature':
        degC = (imperial - 30) * (5/9)
        print('\n',imperial,' degrees F = ',format(degC,',.1f'),' degrees C', sep='')
    elif measure == 'gallons':
        litr = imperial * gal_to_L
        print('\n',imperial,' gallons = ',format(litr,',.1f'),' liters', sep='')
    elif measure == 'pounds':
        kg = imperial * lb_to_kg
        print('\n',imperial,' pounds = ',format(kg,',.1f'),' kilograms', sep='')
    else:
        cm = imperial * in_to_cm
        print('\n',imperial,' inches = ',format(cm,',.1f'),' centimenters', sep='')
        global valid
        valid = False

main()