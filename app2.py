birth_year = input('Birth year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)

weight_lb = input('How many pounds do you weigh? ')
weight_kg = int(weight_lb) / 2.2

print('Nick weighs ' + str(weight_kg) + ' kilograms')