class Employee:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
john = Employee('John')
print(john) # John

#----------------------------

# Dog class
class Dog:
  # Method of the class
  def bark(self):
    print("Ham-Ham")
 
# Create a new instance
charlie = Dog()
 
# Call the method
charlie.bark()
# This will output "Ham-Ham"

#-----------------------------

class Car:
  "This is an empty class"
  pass
 
# Class Instantiation
ferrari = Car()

#-----------------------------

class my_class:
  class_variable = "I am a Class Variable!"
  
x = my_class()
y = my_class()
 
print(x.class_variable) #I am a Class Variable!
print(y.class_variable) #I am a Class Variable!

#-----------------------------


class Animal:
  def __init__(self, voice):
    self.voice = voice
 
# When a class instance is created, the instance variable
# 'voice' is created and set to the input value.
cat = Animal('Meow')
print(cat.voice) # Output: Meow
 
dog = Animal('Woof') 
print(dog.voice) # Output: Woof

#-------------------------------

a = 1
print(type(a)) # <class 'int'>
 
a = 1.1
print(type(a)) # <class 'float'>
 
a = 'b'
print(type(a)) # <class 'str'>
 
a = None
print(type(a)) # <class 'NoneType'>

#-------------------------------

# Defining a class
class Animal:
  def __init__(self, name, number_of_legs):
    self.name = name
    self.number_of_legs = number_of_legs

#-----------------------------

class Employee:
  def __init__(self, name):
    self.name = name
 
  def print_name(self):
    print("Hi, I'm " + self.name)
 
 
print(dir())
# ['Employee', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'new_employee']
 
print(dir(Employee))
# ['__doc__', '__init__', '__module__', 'print_name']

#---------------------------

#<class '__main__.CoolClass'>

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
