def say(text):
    print('==> ' + text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

  def greet(name):
      print(f"Hello, {name}!")

  greet("Alice")
  greet("Bob")

def add(a, b):
    return a + b

two_and_three = add(2, 3)  # This will return 5, but we are not printing it
print(two_and_three)  # Now we print the result of the addition

def is_digit(char):
    if char >= '0' and char <= '9':
        return True
    
    return False