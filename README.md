# Avatar: The Last AirBender - Object-Oriented Programming Lab :fire: :ocean: :rock: :tornado:

## Avatar: The Last AirBender - Object-Oriented Programming Lab

### Preview

Dive into the world of Avatar: The Last AirBender and learn Object-Oriented Programming (OOP) through elemental bending! Create classes for Waterbending, Firebending, Earthbending, and Airbending, each with unique abilities. Your journey will involve mastering Python OOP concepts and passing tests inspired by this beloved series.

### The Elements

1. **Water Bending**: Emulate Katara's fluidity.
2. **Earth Bending**: Channel Toph's strength.
3. **Fire Bending**: Harness Ozai's intensity.
4. **Air Bending**: Embrace Aang's peaceful power.


### Learning Goals

- Create and instantiate classes in Python.
- Build methods that perform functions tailored to their unique objects.
- Use the `property()` function to create properties and validate input.
- Learn test-driven development, and enhance your classes with creative features to master the art of OOP in the Avatar world.

***

### Key Vocab

- **Class**: a bundle of data and functionality. Can be copied and modified to
accomplish a wide variety of programming tasks.
- **Initialize**: create a working copy of a class using its `__init__`
method.
- **Instance**: one specific working copy of a class. It is created when a
class's `__init__` method is called.
- **Object**: the more common name for an instance. The two can usually be used
interchangeably.
- **Object-Oriented Programming**: programming that is oriented around data
(made mobile and changeable in **objects**) rather than functionality. Python
is an object-oriented programming language.
-**Abstract Base Class**: a class that defines the methods that all of its subclasses must have. Abstract base classes are useful for creating a consistent interface for a group of classes that share some functionality.
- **Function**: a series of steps that create, transform, and move data.
- **Method**: a function that is defined inside of a class.
- **Magic Method**: a special type of method in Python that starts and ends
with double underscores. These methods are called on objects under certain
conditions without needing to use their names explicitly. Also called **dunder
methods** (for **double** **underscore**).
- **Attribute**: variables that belong to an object.
- **Property**: attributes that are controlled by methods.

***

### The Avatar World

Welcome to the world of Avatar: The Last AirBender, where the elements of Water, Earth, Fire, and Air hold immense power. In this world, people known as **benders** can manipulate these elements to perform incredible feats.

### Your Journey

Your journey begins with coding challenges to create classes that embody these elements. Each class represents a different element and character. For example, you will craft a `WaterBender` class to encapsulate the abilities of a Water Bender like Katara.

In the spirit of the Avatar world, you will enhance these classes with methods that mimic the unique powers of each element and character. You will be able to boost power, freeze enemies, heal, and perform other fantastic actions.

### Your Quest

Your quest is to pass a series of tests that validate your mastery of Object-Oriented Programming. These tests will evaluate your ability to create and instantiate classes, implement methods, and ensure that your code behaves as expected.

The test-driven development approach will guide your journey. You'll start with failing tests and work your way through each challenge until all tests are successfully passed. Along the way, feel free to add your own creative features to enhance the experience.

Are you ready to embark on this exciting coding adventure in the world of Avatar: The Last Air Bender? Let's get started!

*Note: You can find the challenges and tests in the `lib` and `testing` folders. You will work on the `WaterBender` class and its tests initially.*

Happy coding, young Bender!

***

### The Bender Interface

To ensure a consistent interface for all benders, we introduce the concept of an abstract base class named "Bender." This interface defines the common methods that every bending class should implement.

This abstract base class, "Bender," serves as an interface that outlines the required methods for all bender classes to implement. It ensures a consistent structure and behavior for all bending classes in the Avatar world.

## Instructions

This lab is test-driven. You will write your code in `lib/water_bender.py` and `lib/fire_bender.py`. Run the tests and work your way through the test errors one by one until you get everything passing.

You're also encouraged to look at the test files to see what the tests are expecting to be able to do with your classes. These tests won't force you to use everything that you've learned in this module- feel free to add any features that might be useful!

Note that there are separate test files for the different bending classes inside the `testing` folder. If you'd like to run the tests separately for each class, you can specify which test file to run:

```console
$ pytest -x testing/water_bender_test.py

or

$ pytest -x testing/fire_bender_test.py
```
Remember that the optional -x flag makes your tests stop after the first failure- this setting is ideal for test-driven development!

Happy coding!
