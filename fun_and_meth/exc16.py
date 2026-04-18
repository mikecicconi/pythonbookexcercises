def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# function names:
# multiply: defined on line 1, and used on line 9 to invoke it.
# get_num: defined on line 4, and used on lines 7 and 8 to invoke it.
# float: built in function, used on line 5.
# input: built in function, used on line 5.
# print: built in function, used on line 10.
# 
# parameters:
# left, right: defined on line 1, and used on line 2 to multiply.
# prompt: defined on line 4, and used within function definition on line 5.