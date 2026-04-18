#Without running the following code, what do you think it will do?

def foo(first, second, third=3):
    print(first)
    print(second)
    print(third)

foo(42)

#error because there is not a third value given or default given, since second has default the next one would need
#DEFAULT as well or a value given. this would not raise an error if third was the only one set to default since there
#are no parameters after it.