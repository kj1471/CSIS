---
title: Pygame Workshop Two
author: Kieran Vickers
---

# Starter
## Rules
You have (around) 5 minutes to complete three challenges (on the next slide). 
You must use Python. You must type **as little** as you can, but you can copy-paste
as much as you wish. You may add comments.\
Get a browser and IDLE open...

## Challenges
Typing as little code as you can, but using copy-paste as much as you need:
- Create a function that prints the first n numbers in the Fibonacci sequence
- Create a function that plays FizzBuzz given a number (3/5 version)
- Create a file that plays space invadors using PyGame

# What we aim to cover

## What we aim to cover
- Introduce OO in Python
- Cover inheritance in Python
- Introduce OO concepts to PyGame

## You will need
- ...IDLE open (try `import pygame` now)
- ...A broswer open on a search engine
- ...A browser open on the **Pygame Docs**
- ...to be willing to ask questions

# Main
## Objects objects objects
Have a look at task0.py. Can you spot the redundancy? There are a lot of class
attributes that are repeated, which we could instead inherit.

Can you suggest a class hierarchy (with attribute list) for these classes?

## Discuss
Do we agree the hierarchy?

## Classes
Classes in python are defined using the `class` keyword. In Object-Oriented 
programming we aim to collect the data representing objects of a single type into
a class, along with the functions that act on this data.

## Classes
```python
class Dog:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def greet(self):
        return f"Hello, {self.name}, who's a good dog?"
```

## Inheritance
Given a hierarchical structure of classes, we can inherit attributes and 
functionality from a parent class, then add more attributes and functions.

In Python, we can call `super()` to invoke the parent or superclasses method. For
example, on the next slide see how we use `super().__init__()`. It is considered a
must to call this in any class that inherits and overrides `__init__`.

## Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}."

class Human(Animal):
    def __init__(self, name, languages_spoken):
        super().__init__(name)
        self.languages_spoken = languages_spoken
    def speaks(self):
        return ", ".join(self.languages_spoken)
```

## Inheritance Task
Take *task0.py* and rewrite it so that you only define each attribute once.

The code at the bottom should still run and give the same output after your changes.

## Overriding Methods
When we inherit from a parent/super class, objects of the child class will have 
all the attributes and methods of its parents, exactly the same.

## Overriding Methods
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}."

class Human(Animal):
    pass
```

## Overriding Methods
When we inherit from a parent/super class, objects of the child class will have 
all the attributes and methods of its parents, exactly the same.

You can then override the functions of the parent class in the child class. The
most common function to override is the `__init__` function, but you can override
any function.

## Overriding Task
Look at *task1.py*. It is an example answer to the previous task, with functions 
added to access the attributes. Replace the print statements with different print 
statements that use these functions. Can you write another function in a child
class that overrides a parent class's function?


# Pygame
## Pygame
So, object oriented pygame, why is this useful?

# See you next session!
## See you in two weeks time!  
Next session:
