print('\n===== IMPERIAL TO METRIC CONVERSION CALCULATOR =====')
print('=' * 52)

#conversion constants
mi_to_km = 1.60
gal_to_L = 3.90
lb_to_kg = 0.45
in_to_cm = 2.54
#attempt constant for limited attempt looping data validation
attempt = 0
#max attempts allowed (data validation) constant
max_attempt = 4
#is data valid? constant
valid = False
#message constants
TRY_AGAIN = '\nSorry, this value is not accepted.\n'
TERMINATE = '\nDATA INVALID\nGOODBYE'

#take input and run data validation for "miles to kilometers"
while not valid:
    mi = float(input('Miles: '))
    if(mi < 0):
        valid = False
    else:
        valid = True
    if (not valid):
        print(TRY_AGAIN)
        attempt += 1
        print('You have',max_attempt - attempt,'attempt(s) left.')
        if(attempt >= max_attempt):
            valid = True
            print(TERMINATE)
#reset attempt counter, take input and run data validation for "F to C"
if (valid and attempt < max_attempt):     
    valid = False    
    attempt = 0
    while not valid:
        degF = float(input('\nTemperature (F): '))
        if(degF > 1000):
            valid = False
        else:
            valid = True
        if (not valid):
            print(TRY_AGAIN)
            attempt += 1
            print('You have',max_attempt - attempt,'attempt(s) left.')
            if(attempt >= max_attempt):
                valid = True
                print(TERMINATE)
#reset attempt counter, take input, and run data validation for "gallons to liters"
if (valid and attempt < max_attempt): 
    valid = False
    attempt = 0
    while not valid:
        gal = float(input('\nGallons: '))
        if(gal < 0):
            valid = False
        else:
            valid = True
        if (not valid):
            print(TRY_AGAIN)
            attempt += 1
            print('You have',max_attempt - attempt,'attempt(s) left.')    
            if(attempt >= max_attempt):
                valid = True
                print(TERMINATE)
#reset attempt counter, take input, and run data validation for "pounds to kilograms"
if (valid and attempt < max_attempt):
    valid = False
    attempt = 0
    while not valid:
        lb = float(input('\nDry pounds: '))
        if (lb < 0):
            valid = False
        else:
            valid = True
        if (not valid):
            print(TRY_AGAIN)
            attempt += 1
            print('You have',max_attempt - attempt,'attempt(s) left.')
            if(attempt >= max_attempt):
                valid = True
                print(TERMINATE)
#reset attempt counter, take input, and run data validation for "inches to centimeters"        
if(valid and attempt < max_attempt):
    valid = False
    attempt = 0
    while not valid:
        inches = float(input('\nInches: '))
        if (inches < 0):
            valid = False
        else:
            valid = True
        if (not valid):
            print(TRY_AGAIN)
            attempt += 1
            print('You have',max_attempt - attempt,'attempt(s) left.')
            if(attempt >= max_attempt):
                valid = True
                print(TERMINATE)
if(valid and attempt < max_attempt):
    #run calculations
    km = mi * mi_to_km
    degC = (degF - 32) * (5/9)
    L = gal * gal_to_L
    kg = lb * lb_to_kg
    cm = inches * in_to_cm
    #display output
    print('\n======================RESULTS=======================')
    print('=' * 52)
    print('\n',mi,' miles = ',format(km,'.1f'),' kilometres.\n',sep='')
    print(degF,'degrees Fahrenheit =',format(degC,'.1f'),'degrees Centigrade.\n')
    print(gal,'gallons =',format(L,'.1f'),'litres.\n')
    print(lb,'pounds =',format(kg,'.1f'),'kilograms.\n')
    print(inches,'inches =',format(cm,'.1f'),'centimetres.\n')