import abc
import mod_4
from abc import ABC, abstractmethod
# modularity is achieved by importing mod_4 for its function show()
# hierarchy is achieved by base class and derived classes
class Animal(ABC):
    #this is an abstract base class
    @abc.abstractmethod
    def display(self):
        pass


class Dog(Animal):

    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Dog("Dog", 4, "bark")
obj.display()


class Cat(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Cat("cat", 4, "meow")
obj.display()


class Cow(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Cow("Cow", 4, "moo")
obj.display()


class Tiger(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Tiger("Tiger", 4, "roar")
obj.display()


class Elephant(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Elephant("elephant", 4, "trumpet")
obj.display()


class Hen(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Hen("Hen", 2, "cluck")
obj.display()


class Camel(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Camel("Camel", 4, "grunt")
obj.display()


class Bear(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Bear("Bear", 2, "growl")
obj.display()


class Frog(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Frog("Frog", 4, "croak")
obj.display()


class Pig(Animal):
    def __init__(self, name, sound, legs):
        self.Name = name
        self.Sound = sound
        self.Legs = legs

    def display(self):
        print("Name: {} Sound: {} Legs: {}".format(self.Name, self.Sound, self.Legs))


obj = Pig("Pig", 4, "squeak")
obj.display()


class Circle:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Circle("Circle", "pi * radius^2")
mod_4.show(obj)


class Square:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object

obj = Square("Square", "side^2")
mod_4.show(obj)


class Rectangle:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Rectangle("Rectangle", "length * width")
mod_4.show(obj)


class Triangle:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Triangle("Triangle", "1/2 * base * height")
mod_4.show(obj)

class Parallelogram:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Parallelogram("Parallelogram", "breadth * height")
mod_4.show(obj)


class Trapezium:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Trapezium("Trapezium", "1/2 * (side1 + side2) * height")
mod_4.show(obj)


class Ellipse:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Ellipse("Ellipse", "pi * a * b")
mod_4.show(obj)


class Cube:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Cube("Cube", "6 * a^2")
mod_4.show(obj)


class Sphere:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Sphere("Sphere", "4 * pi * r^2")
mod_4.show(obj)


class Hemisphere:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    # creating object
obj = Hemisphere("Hemisphere", "3 * pi * r^2")
mod_4.show(obj)

