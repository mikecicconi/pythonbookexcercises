
# Write a program named age.py that asks the user to enter their age, 
# then calculates and reports the future age 10, 20, 30, and 40 years from now.

age = int(input('How old are you? '))
print()
print(f'You are {age} years old.')
for years in [10, 20, 30, 40]:

    print(f'In {years} years, you will be {age + years} years old.')