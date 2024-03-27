# Python-Week-1-to-4
![Python Logo](https://www.python.org/static/img/python-logo.png)
<br>
Capaciti : Python Week 1 to 4

# A Week One : Summary

__Data Types:__

* Numeric Types: Integers (int), floating-point numbers (float), and complex numbers (complex).
* Sequence Types: Lists (list), tuples (tuple), and strings (str).
* Mapping Type: Dictionary (dict).
* Set Types: Set (set) and frozen set (frozenset).
* Boolean Type: Boolean (bool).

__Data Structures:__

* Lists: Ordered collection of items that can be changed (mutable).
* Tuples: Ordered collection of items that cannot be changed (immutable).
* Dictionaries: Collection of key-value pairs, where each key maps to a value.
* Sets: Unordered collection of unique items, useful for mathematical operations like union, intersection, etc.

__Control Flow:__

* Conditional Statements: if, elif, and else for executing different blocks of code based on conditions.
* Loops: for loop for iterating over a sequence, while loop for executing a block of code repeatedly as long as a condition is true.

__Functions:__

* Defining Functions: def keyword to define functions.
* Arguments and Return Values: Functions can take arguments (inputs) and return values (outputs).

__Object-Oriented Programming (OOP):__

* Classes and Objects: Classes are blueprints for creating objects with attributes and method

# A Week Two : Summary

__Functions:__

def functionName(parameters):
code
return 
* args
* **kwargs

__Functions:__

* Text Processing in Python:
> text = "Insert Text Here"
punctuations = [',' , '.' , '*']
text = text.lower()
for punctuation in punctuations:
    text = text.replace(punctuation, '')
text = text.replace('\n' , ' ')
text = ' '.join([word for word in text.split() if len(word) > 3])

__Lambda:__


>double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(age_check(18))

__Class Inheritance:__

>Define a superclass called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

Define a subclass called Dog, which inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

Define another subclass called Cat, which also inherits from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

Create instances of the Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

Call the speak method on the instances
print(dog.speak())  # Output: Buddy says woof!
print(cat.speak())  # Output: Whiskers says meow!

# A Week Three : Summary

* AssertionError : Raised when an assert statement fails.
* AttributeError : Raised when attribute assignment or reference fails.
* EOFError : Raised when the input() function hits end-of-file condition.
* FloatingPointError : Raised when a floating point operation fails.
* GeneratorExit : Raise when a generator's close() method is called.
* ImportError : Raised when the imported module is not found.
* IndexError : Raised when the index of a sequence is out of range.
* KeyError : Raised when a key is not found in a dictionary.
* KeyboardInterrupt : Raised when the user hits the interrupt key (Ctrl+C or Delete).
* MemoryError : Raised when an operation runs out of memory.
* NameError : Raised when a variable is not found in local or global scope.
* NotImplementedError : Raised by abstract methods.
* OSError : Raised when system operation causes system related error.
* OverflowError : Raised when the result of an arithmetic operation is too large to be represented.
* ReferenceError : Raised when a weak reference proxy is used to access a garbage collected referent.
* RuntimeError : Raised when an error does not fall under any other category.
* StopIteration : Raised by next() function to indicate that there is no further item to be returned by iterator.
* SyntaxError : Raised by parser when syntax error is encountered.
* IndentationError : Raised when there is incorrect indentation.
* TabError : Raised when indentation consists of inconsistent tabs and spaces.
* SystemError : Raised when interpreter detects internal error.
* SystemExit : Raised by sys.exit() function.
* TypeError : Raised when a function or operation is applied to an object of incorrect type.
* UnboundLocalError : Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
* UnicodeError : Raised when a Unicode-related encoding or decoding error occurs.
* UnicodeEncodeError : Raised when a Unicode-related error occurs during encoding.
* UnicodeDecodeError : Raised when a Unicode-related error occurs during decoding.
* UnicodeTranslateError : Raised when a Unicode-related error occurs during translating.
* ValueError : Raised when a function gets an argument of correct type but improper value.
* ZeroDivisionError : Raised when the second operand of division or modulo operation is zero.


Open a file:

>Open and read a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


Appending a file:

>Append content to a file
with open('example.txt', 'a') as file:
    file.write('\nThis is additional content.')

Adding content to file:

>Add content to a file (overwrite existing content)
with open('example.txt', 'w') as file:
    file.write('This is new content.')


