credit = input('What is your credit score? ')
credit = int(credit)
if credit > 600:
    good_credit = True
else:
    good_credit = False

house_price = 1000000
if good_credit:
    down_payment = 0.10 * house_price
else:
    down_payment = 0.20 * house_price

print(f'The down payment required is ${down_payment}')
