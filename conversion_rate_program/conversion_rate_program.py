print('\n===== IMPERIAL TO METRIC CONVERSION CALCULATOR =====')
print('=' * 52)

#conversion constants
mi_to_km = 1.60
gal_to_L = 3.90
lb_to_kg = 0.45
in_to_cm = 2.54
#attempt constant for limited attempt looping data validation
attempt = 0
#max attempt constant
max_attempt = 3
#message constants
TRY_AGAIN = '\nSorry, negative values are not accepted. Try again.\n'
TERMINATE = '\nDATA INVALID\nGOODBYE'


mi = float(input('Miles: '))
while(mi < 0 and attempt < max_attempt):
    print(TRY_AGAIN)
    print('You have',max_attempt - attempt,'tries left.')
    mi = float(input('Miles: '))
    attempt = attempt + 1
if(mi < 0 and attempt >= max_attempt):    #if third try is still invalid, end program
    print(TERMINATE)
else:
    attempt = 0     #reset number of tries allowed
    degF = float(input('\nTemperature (F): '))
    while(degF > 1000 and attempt < max_attempt):
        print(TRY_AGAIN)
        print('You have',max_attempt - attempt,'tries left.')
        degF = float(input('\nTemperature (F): '))
        attempt = attempt + 1
    if(degF > 1000 and attempt >= max_attempt):
        print(TERMINATE)
    else:
        attempt = 1
        gal = float(input('\nGallons: '))
        while(gal < 0 and attempt < max_attempt):
            print(TRY_AGAIN)
            print('You have',max_attempt - attempt,'tries left.')
            gal = float(input('Gallons: '))
            attempt = attempt + 1
        if(gal < 0 and attempt >= max_attempt):
            print(TERMINATE)
        else:
            attempt = 1
            lb = float(input('\nDry pounds: '))
            while(lb < 0 and attempt < max_attempt):
                print(TRY_AGAIN)
                print('You have',max_attempt - attempt,'tries left.')
                lb = float(input('\nDry pounds: '))
                attempt = attempt + 1
            if(lb < 0 and attempt >= max_attempt):
                print(TERMINATE)
            else:
                attempt = 1
                inches = float(input('\nInches: '))
                while(inches < 0 and attempt < max_attempt):
                    print(TRY_AGAIN)
                    print('You have',max_attempt - attempt,'tries left.')
                    inches = float(input('\nInches: '))
                    attempt = attempt + 1
                if(inches < 0 and attempt >= max_attempt):
                    print(TERMINATE)
                else:
                    #run calculations
                    km = mi * mi_to_km
                    degC = (degF - 32) * (5/9)
                    L = gal * gal_to_L
                    kg = lb * lb_to_kg
                    cm = inches * in_to_cm
                    #display output
                    print('=======================RESULTS======================')
                    print('=' * 52)
                    print('\n',mi,' miles = ',format(km,'.1f'),' kilometres.\n',sep='')
                    print(degF,'degrees Fahrenheit =',format(degC,'.1f'),'degrees Centigrade.\n')
                    print(gal,'gallons =',format(L,'.1f'),'litres.\n')
                    print(lb,'pounds =',format(kg,'.1f'),'kilograms.\n')
                    print(inches,'inches =',format(cm,'.1f'),'centimetres.\n')
                    
