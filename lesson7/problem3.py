print('-' * 70)
print('Year when you turn 100')
print()

print('Description: This will tell you what year you will turn 100.')
print()

current = input('Current year: ')
current = int(current)
age = input('How old are you?: ')
age = int(age)
born = current - age
future = born + 100
future = str(future)

print('You will turn 100 in the year ' + future)