# decorators  - are functions that wraps around other functions/methods to add functionality(authentication, logging, caching, access control to methods or class) to them
# Decorator function to log method calls
# def log_method_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling method: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# # Example class with a method decorated with log_method_call
# class MyClass:
#     @log_method_call
#     def my_method(self):
#         print("Executing my_method")

# # Create an object of MyClass
# obj = MyClass()

# # Call the decorated method
# obj.my_method()
'''
*args - arguments are passed to the functions are collected in a tuple.
    use it to define functions that can accept any number of positional arguments
    
**kwargs - allows you to pass variable number of keyword argument       (key-value pairs) to the functions
    keyword argument are collected into a dictionary can be accessed using kwargs or name you made(same with args)

'''

def example_function(*args, **kwargs):
    print("Positional arguments: "+ args)
    print("Keyword arguments: "+ kwargs)

example_function(1,2,3, name="Älice", age=21)

'''
Here's how inheritance works:

A class that inherits from another class is called a subclass or derived class.
The class from which the subclass inherits is called the superclass or base class.

'''
'''

# Define a superclass called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Define a subclass called Dog, which inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

# Define another subclass called Cat, which also inherits from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# Create instances of the Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on the instances
print(dog.speak())  # Output: Buddy says woof!
print(cat.speak())  # Output: Whiskers says meow!


'''