def main():
    import convert
    convert.intro()
    mi = float(input('Miles: '))
    unit = 'miles'
    valid, mi = convert.validate_neg(mi, unit)
    if valid:
        km = convert.run_conversion(mi, unit)
        print('\n',mi,' miles = ',format(km,',.1f'),' kilometers', sep='')
    if valid:
        degF = float(input('\n\nDegrees F: '))
        unit = 'temperature'
        valid, degF = convert.validate_temp(degF, unit)
        if valid:
            degC = convert.run_conversion(degF, unit)
            print('\n',degF,' degrees F = ',format(degC,',.1f'),' degrees C', sep='')
    if valid:
        gal = float(input('\n\nGallons: '))
        unit = 'gallons'
        valid, gal = convert.validate_neg(gal, unit)
        if valid:
            litr = convert.run_conversion(gal, unit)
            print('\n',gal,' gallons = ',format(litr,',.1f'),' liters', sep='')
    if valid:
        lb = float(input('\n\nDry pounds: '))
        unit = 'pounds'
        valid, lb = convert.validate_neg(lb, unit)
        if valid:
            kg = convert.run_conversion(lb, unit)
            print('\n',lb,' pounds = ',format(kg,',.1f'),' kilograms', sep='')
    if valid:
        inches = float(input('\n\nInches: '))
        unit = 'inches'
        valid, inches = convert.validate_neg(inches, unit)
        if valid:
            cm = convert.run_conversion(inches, unit)
            print('\n',inches,' inches = ',format(cm,',.1f'),' centimenters', sep='')

main()