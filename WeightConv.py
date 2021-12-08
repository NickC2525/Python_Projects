weight = float(input('Weight: '))
unit = input('Enter K for kilograms or P for pounds ')

if unit.upper() == 'K':
    weight2 = weight * 2.2
    print(f'Your weight in pounds is {weight2}')
elif unit.upper() == 'P':
    weight2 = weight / 2.2
    print(f'Your weight in kilograms is {weight2}')
else:
    print('Invalid entry')
