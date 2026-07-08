# DSA

This repository is used to track DSA practice problems and Python learning exercises.

## Table of Contents
- [Deque Keywords](#deque-keywords)
  - [append](#append)
  - [appendleft](#appendleft)
  - [pop](#pop)
  - [popleft](#popleft)
  - [extend](#extend)
  - [extendleft](#extendleft)
  - [rotate](#rotate)
- [Counter Keywords](#counter-keywords)
  - [Counter](#counter)
  - [elements()](#elements)
  - [most_common()](#most_common)
  - [update()](#update)
  - [subtract()](#subtract)
  - [addition and subtraction](#addition-and-subtraction)
  - [intersection and union](#intersection-and-union)

## Contents
- [basic_python.py](basic_python.py): basic Python examples covering variables, arithmetic, input handling, conditionals, loops, and functions.
- [deque.py](deque.py): a hands-on example of Python's collections.deque operations such as append, appendleft, pop, popleft, extend, extendleft, and rotate.
- [counter.py](counter.py): a practice script demonstrating Python's Counter class and its common operations.
- [hello_world.py](hello_world.py): a simple introductory script.
- [test_initial_code.py](test_initial_code.py): initial verification tests for the repository.

## Deque Keywords
### append
Adds an element to the right end of the deque.

### appendleft
Adds an element to the left end of the deque.

### pop
Removes and returns the rightmost element from the deque.

### popleft
Removes and returns the leftmost element from the deque.

### extend
Adds multiple elements to the right side of the deque.

### extendleft
Adds multiple elements to the left side of the deque. The order of the supplied elements is reversed.

### rotate
Rotates the deque by a given number of positions. A positive value moves items to the right, while a negative value moves them to the left.

## Counter Keywords
### Counter
A Counter is a dictionary subclass used to count hashable objects such as numbers or strings.

### elements()
Returns an iterator over each element repeated as many times as its count.

### most_common()
Returns the most common elements, optionally limited to a given number of results.

### update()
Adds counts from another iterable or Counter.

### subtract()
Decreases counts using values from another iterable or Counter.

### Addition and subtraction
Counters can be added or subtracted to combine or remove counts.

### Intersection and union
The & operator keeps the minimum counts, while the | operator keeps the maximum counts.

## How to run
- python3 basic_python.py
- python3 deque.py
- python3 counter.py
- python3 hello_world.py

## Notes
The scripts are intended for learning and practicing core Python concepts alongside DSA topics.
