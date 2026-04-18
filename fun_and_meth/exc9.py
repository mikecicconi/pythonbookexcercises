#Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.1718)

#converts the two floats to '2' and '3'
#what actually happens: we are setting a default for the second value and third value.

