print('IMPERIAL TO METRIC CALCULATOR\n')

# defines constants for conversion rates

mi_to_km = 1.6                                                             # conversion rate from miles to kilometres
gal_to_L = 3.9                                                             # conversion rate from gallons to litres
lb_to_kg = 0.45                                                            # conversion rate from pounds to kilograms
inch_to_cm = 2.54                                                          # conversion rate from inches to centimetres

# receives input for calculations; assigning variables

mi = float(input('Miles: '))
degF = float(input('Degrees Fahrenheit: '))
gal = float(input('Gallons: '))
lb = float(input('Dry pounds: '))                                          # specifies dry pounds to avoid confusion with pounds sterling
inch = float(input('Inches: '))

# performs calculations

km = mi * mi_to_km
degC = (degF - 32) * (5/9)
L = gal * gal_to_L
kg = lb * lb_to_kg
cm = inch * inch_to_cm

# displays output for user to nearest tenth of a unit for neater, consistent viewing

print('\n',mi,' miles = ',format(km,',.1f'),' kilometres',sep='')                          
print(degF, 'degrees Fahrenheit =',format(degC,'.1f'),'degrees Celsius')   
print(gal,'gallons =',format(L,',.1f'),'litres')
print(lb,'pounds =',format(kg,',.1f'),'kilograms')
print(inch,'inches =',format(cm,',.1f'),'centimetres')
