# 0x13. JavaScript - Objects, Scopes and Closures

### Author

Solomon - [GitHub Profile](https://github.com/SolomonOdunusi)

## Introduction

This project focuses on JavaScript, specifically covering topics related to objects, scopes, and closures. The tasks aim to enhance your understanding of object-oriented programming concepts in JavaScript.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why JavaScript programming is amazing
- Create an object in JavaScript using the class notation
- Understand the meaning of `this` in JavaScript
- Grasp the importance of variable type and scope
- Comprehend the concepts of closure and prototype
- Inherit an object from another in JavaScript

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using Node (version 14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Code should be semistandard compliant, following the rules of Standard with semicolons on top
- All files must be executable
- Do not use `var`

## Setup

To install Node 14, use the following commands:

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

To install `semistandard`, use:

```bash
$ sudo npm install semistandard --global
```

## Tasks Overview

### 0. Rectangle #0

Write an empty class `Rectangle` that defines a rectangle using the class notation.

### 1. Rectangle #1

Write a class `Rectangle` that defines a rectangle, taking width (`w`) and height (`h`) as arguments.

### 2. Rectangle #2

Extend the `Rectangle` class with additional conditions: if `w` or `h` is equal to 0 or not a positive integer, create an empty object.

### 3. Rectangle #3

Enhance the `Rectangle` class by adding an instance method `print()` that prints the rectangle using the character 'X'.

### 4. Rectangle #4

Extend the `Rectangle` class with two instance methods: `rotate()` and `double()`.

### 5. Square #0

Write a class `Square` that defines a square and inherits from `Rectangle`. The constructor should take a single argument `size`.

### 6. Square #1

Extend the `Square` class with an instance method `charPrint(c)` that prints the rectangle using the character `c` (default is 'X').

### 7. Occurrences

Write a function that returns the number of occurrences of a value in a list.

### 8. Esrever

Write a function that returns the reversed version of a list without using the built-in `reverse` method.

### 9. Log me

Write a function that prints the number of arguments already printed and the new argument value.

### 10. Number conversion

Write a function that converts a number from base 10 to another base passed as an argument.

### 11. Factor index

Write a script that imports an array and computes a new array. The new array should have each value equal to the value of the initial list multiplied by its index.

### 12. Sorted occurrences

Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

### 13. Concat files

Write a script that concatenates two files.

## Usage

To run the scripts, use the following format:

```bash
$ ./script_name.js
```

