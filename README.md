# Avatar: The Last AirBender - Python Object-Oriented Programming Lab :fire: :ocean: :rock: :tornado:

## Table of contents

- [Avatar: The Last AirBender - Python Object-Oriented Programming Lab :fire: :ocean: :rock: :tornado:](#avatar-the-last-airbender---python-object-oriented-programming-lab-fire-ocean-rock-tornado)
  - [Table of contents](#table-of-contents)
  - [Preview](#preview)
  - [Learning Goals](#learning-goals)
  - [Your Journey](#your-journey)
    - [Your Quest](#your-quest)
  - [Getting Started](#getting-started)
    - [Creating a new venv](#creating-a-new-venv)
      - [The libraries are too old](#the-libraries-are-too-old)
    - [Running the tests](#running-the-tests)
      - [It doesn't work / there's a problem](#it-doesnt-work--theres-a-problem)
      - [View the test coverage report](#view-the-test-coverage-report)

## Preview

Dive into the world of Avatar: The Last Air Bender
and learn Python through elemental bending!
Create classes for
Waterbending, Firebending, Earthbending, and Airbending,
each with unique abilities.
Your journey will involve mastering Python and OOP concepts, and
passing tests inspired by the beloved series.

## Learning Goals

- Create and instantiate classes in Python.
- Build methods that perform functions tailored to their unique objects.
- Read Tests to understand Python.
- Use the `property()` function to create properties and validate input.
- Learn test-driven development,
and enhance your classes with creative features to master the art of OOP in the Avatar world.
- Get to know the big world of python.

## Your Journey

Your journey begins with coding challenges to create classes that embody these elements.
Each class represents a different element and character.
For example, you will craft a `WaterBender` class to encapsulate the abilities of a Water Bender like Katara.

### Your Quest

Your quest is to pass a series of tests that
validate your mastery of Python and OOP.
These tests will evaluate your ability to
create and instantiate classes,
implement methods,
and ensure that your code behaves as expected.

The test-driven development approach will guide your journey.
You'll start with failing tests and work your way
through each challenge until all tests are successfully passed.
To run the tests, use the `noxfile`
as explained [here](#running-the-tests).

Along the way,
feel free to add your own creative features to enhance the experience.
For example: a base class, protected methods,
the signatures of the methods, and more.
But you **must not** break and/or change the tests, configs,
the `noxfile.py`, and the `Poetry` files.

Are you ready to embark on this exciting coding
adventure in the world of
Avatar: The Last Air Bender? Let's get started!

Happy coding, young Bender!

## Getting Started

This project uses `Poetry` (version 1.7.1 or above),
`nox`, and many more tools.
So in this guide would guide you on how to prepare your environment.

You would need to install the tool `Poetry` first,
which you can can download from
[here](https://python-poetry.org/docs/#installation).

### Creating a new venv

Run the command:

```bash
poetry install
```

To create a new venv with all the project's dependencies.
You can activate the venv's shell with the command:

```bash
poetry shell
```

If it doesn't work, just activate the venv yourself.
You can read about it
[here](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments).

#### The libraries are too old

If you want to, you should update the used libraries with the
command:

```bash
poetry update
```

If you need to make a bigger change (like updating a major),
you should talk with your mentor first!

### Running the tests

Now, to run the tests and check if you have finished the exercise,
you just need to run `nox`
(from the shell you have activated [here](#creating-a-new-venv)):

```bash
nox
```

what it does is that it runs the `session`s defined at the
`noxfile.py` file, and there it's defined to run the tests.

You can view and/or use the outputs of the tests
from the created files or from your shell's `stdout`.

#### It doesn't work / there's a problem

If you think there's a problem with the tests, or there's
a problem with the configs or something else,
you should talk with your mentor.

#### View the test coverage report

You can view the test coverage report as a nice web page
at the generated file:

```path
html_cov/index.html
```
