#What does this program print? Why?

foo = 'bar' #global scope

def set_foo():
    foo = 'qux' #local scope

set_foo()
print(foo)