#defines variables

payroll_year = 2019                               #current fiscal year

BaseSal = 2000                                    #base salary

ComTier1 = 0.00                                   #commission rates
ComTier2 = 0.02
ComTier3 = 0.15
ComTier4 = 0.28
ComTier5 = 0.35

BonTier1 = 0.00                                   #bonus rates
BonTier2 = 0.00
BonTier3 = 1000.00
BonTier4 = 5000.00
BonTier5 = 100000.00

#assigns variables to input

name = input('Employee name: ')
start_month = int(input('Employee start month (MM): '))
start_year = int(input('Employee start year (YYYY): '))
payroll_month = int(input('\nMonth you are reporting sales for (MM): '))
sales = float(input('Employee sales for this month: $'))
vacation = float(input('Enter your vacation time (days) used for this month: '))

#calculations

long_month = payroll_month - start_month          #calculates longevity
long_year = payroll_year - start_year

if(long_month < 0):                               #rounds down to nearest COMPLETE years
     Longevity = long_year - 1
     longevity = (Longevity * 12) - long_month    #total months worked
else:
     longevity = (long_year * 12) + long_month    #total months worked



if(sales < 10000):                                #determines commission and bonus rate tiers
     com = ComTier1
     bon = BonTier1
elif(sales >= 10000 and sales <= 100000):
     com = ComTier2
     bon = BonTier2
elif(sales >= 100001 and sales <= 500000):
     com = ComTier3
     bon = BonTier3
elif(sales >= 500001 and sales <= 1000000):
     com = ComTier4
     bon = BonTier4
else:
     com = ComTier5
     bon = BonTier5

if(vacation > 3):                                 #determines deductions
     deduct = -200.00
else:
     deduct = 0.00
                                             
if(longevity >= 3):                               #determines bonuses
     bonus = bon
else:
     bonus = 0

if(longevity >= 60 and sales > 100000):
     add_bonus = 1000.00
else:
     add_bonus = 0.00

#displays pay stub information

print('\n',('.' * 50))
print('\nPAYROLL INFORMATION FOR',name,'\n')                                         #Employee
print('Employee at SoftwarePirates Inc. for ',(longevity / 12),' years.',sep='')     #Longevity
print('\n$',format(BaseSal,'12,.2f'),'..... base pay',sep='')                        #Base pay
print('$',format((com * sales),'12,.2f'),'..... commission',sep='')                  #Commission
print('$',format(bonus,'12,.2f'),'..... sales bonus',sep='')                         #Bonus
print('$',format(add_bonus,'12,.2f'),'..... longevity & sales bonus',sep='')         #Additional bonus
print('$',format(deduct,'12,.2f'),'..... excess vacation time deduction',sep='')     #Deduction

totalSal = (BaseSal + (com * sales) + bonus + add_bonus + deduct)

print('\n$',format(totalSal,'12,.2f'),'..... TOTAL GROSS PAY',sep='')                #Total gross pay

