#defines constants for conversions

mi_to_km = 1.6
gal_to_L = 3.9
lb_to_kg = 0.45
in_to_cm = 2.54

#assigns input to variables
#continuous data valiation; triggers termination as soon as unacceptable data is input

mi = float(input('Miles: '))                                
if (mi < 0):
     print('Sorry, negative values not accepted.\nEND')                                                             #invalidates negative values                                                     
else:
     degF = float(input('\nTemperature (F): '))
     if (degF > 1000):                                                                                              #invalidates data entered for temps above 1000 F
          print('Sorry, value not accepted.\nEND')
     else:
          gal = float(input('\nGallons: '))
          if (gal < 0):
               print('Sorry, negative values not accepted.\nEND')
          else:
               lb = float(input('\nDry pounds: '))
               if (lb < 0):
                    print('Sorry, negative values not accepted.\nEND')
               else:
                    inches = float(input('\nInches: '))
                    if (inches < 0):
                         print('Sorry, negative values not accepted.\nEND') 
                    else:                                                                                           #if all data is valid, triggers calculations
                         km = mi * mi_to_km
                         degC = (degF - 32) * (5/9)
                         L = gal * gal_to_L
                         kg = lb * lb_to_kg
                         cm = inches * in_to_cm

#displays output

                         print('\n','*' * 30)
                         print('\n',mi,' miles = ',format(km,'.1f'),' kilometres.\n',sep='')                
                         print(degF,'degrees Fahrenheit =',format(degC,'.1f'),'degrees Centigrade.\n')
                         print(gal,'gallons =',format(L,'.1f'),'litres.\n')
                         print(lb,'pounds =',format(kg,'.1f'),'kilograms.\n')
                         print(inches,'inches =',format(cm,'.1f'),'centimetres.\n')
                         
