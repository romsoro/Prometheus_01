age = input('Enter your age: ')
try:
    test = int(age)
except:
    test = -1

if test >= 0:
    print(f'Your age is: {age} years')
else:
    print('Need enter a number. Please try again')
