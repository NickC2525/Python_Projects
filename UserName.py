name = input('Please enter your username (Must be between 3 and 20 characters) ')
name_length = len(name)

if name_length < 3:
    print('Name must be at least 3 characters long')
elif name_length > 20:
    print('Name must not exceed 20 characters')
else:
    print('Name is valid')
