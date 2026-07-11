# DSA

This repository is used to track DSA practice problems and Python learning exercises.

## Table of Contents
- [Contents](#contents)
- [Day 1](#day-1)
- [Day 2](#day-2)
- [Day 3](#day-3)
- [Day 4 Modules](#day-4-modules)
  - [random_module.py](#random_modulepy)
  - [default_dict.py](#default_dictpy)
  - [func_tools.py](#func_toolspy)
  - [math_tools.py](#math_toolspy)
  - [named_tuple.py](#named_tuplepy)
  - [ordered_dict.py](#ordered_dictpy)
  - [bisect_tree.py](#bisect_treepy)
- [Deque Keywords](#deque-keywords)
- [Counter Keywords](#counter-keywords)

## Contents
- Day 1
  - [DSA_Day_1/basic_python.py](DSA_Day_1/basic_python.py): basic Python examples covering variables, arithmetic, input handling, conditionals, loops, and functions.
  - [DSA_Day_1/hello_world.py](DSA_Day_1/hello_world.py): a simple introductory script.
  - [DSA_Day_1/test_initial_code.py](DSA_Day_1/test_initial_code.py): initial verification tests for the repository.
- Day 2
  - [DSA_Day_2/deque.py](DSA_Day_2/deque.py): a hands-on example of Python's collections.deque operations such as append, appendleft, pop, popleft, extend, extendleft, and rotate.
- Day 3
  - [DSA_Day_3/counter.py](DSA_Day_3/counter.py): a practice script demonstrating Python's Counter class and its common operations.
- Day 4
  - [DSA_Day_4/random_module.py](DSA_Day_4/random_module.py): examples using the Python random module.
  - [DSA_Day_4/default_dict.py](DSA_Day_4/default_dict.py): examples using defaultdict.
  - [DSA_Day_4/func_tools.py](DSA_Day_4/func_tools.py): examples using functools tools such as lru_cache, reduce, partial, and wraps.
  - [DSA_Day_4/math_tools.py](DSA_Day_4/math_tools.py): examples using the math module.
  - [DSA_Day_4/named_tuple.py](DSA_Day_4/named_tuple.py): examples showing namedtuple usage.
  - [DSA_Day_4/ordered_dict.py](DSA_Day_4/ordered_dict.py): examples showing OrderedDict usage.
  - [DSA_Day_4/bisect_tree.py](DSA_Day_4/bisect_tree.py): examples using the bisect module.

## Day 1
- [DSA_Day_1/basic_python.py](DSA_Day_1/basic_python.py): beginner-friendly Python practice covering variables, arithmetic, input, loops, and functions.
- [DSA_Day_1/hello_world.py](DSA_Day_1/hello_world.py): a simple first program to confirm Python setup.
- [DSA_Day_1/test_initial_code.py](DSA_Day_1/test_initial_code.py): initial verification examples for the repository.

## Day 2
- [DSA_Day_2/deque.py](DSA_Day_2/deque.py): practice with Python deque operations such as append, appendleft, pop, popleft, extend, extendleft, and rotate.

## Day 3
- [DSA_Day_3/counter.py](DSA_Day_3/counter.py): practice with the Counter class, including counting, updating, subtracting, and combining counters.

## Day 4 Modules

### random_module.py
This file demonstrates the Python random module.
- random.random(): returns a floating-point number in the range $[0, 1)$.
- random.randint(a, b): returns a random integer between a and b, inclusive.
- random.randrange(start, stop, step): returns a randomly chosen value from the range using the given step.
- random.choice(sequence): selects a random element from a sequence.
- random.sample(sequence, k): returns k unique random items from a sequence.
- random.uniform(a, b): returns a random floating-point number between a and b.
- random.shuffle(sequence): shuffles the elements of a list in place.

### default_dict.py
This file shows how to use defaultdict from collections.
- defaultdict(int): creates a dictionary that automatically assigns 0 when a missing key is accessed.
- defaultdict(list): creates a dictionary that automatically creates an empty list for missing keys.
- defaultdict(set): creates a dictionary that automatically creates an empty set for missing keys.
- defaultdict(lambda: "N/A"): provides a custom default value for missing keys.

### func_tools.py
This file covers functools utilities.
- lru_cache: caches recent function calls to improve performance for repeated computations.
- reduce: combines a sequence into a single value using a function.
- partial: creates a new function with some arguments pre-filled.
- wraps: preserves metadata like the original function name and docstring in a decorator wrapper.

### math_tools.py
This file demonstrates common math functions from the math module.
- math.pi and math.e: constant values used in mathematical calculations.
- math.sqrt(): returns the square root of a number.
- math.pow(): raises a number to a power.
- math.factorial(): returns the factorial of a number.
- math.gcd(): returns the greatest common divisor.
- math.lcm(): returns the least common multiple.
- math.log(), math.log10(), and math.log2(): compute logarithms.
- math.ceil() and math.floor(): round numbers up or down.
- math.isfinite() and math.isinf(): check whether a number is finite or infinite.

### named_tuple.py
This file shows how namedtuple helps create readable fixed-record data structures.
- namedtuple: creates a tuple subclass with named fields.
- _replace(): creates a new named tuple with specific field values updated.

### ordered_dict.py
This file demonstrates OrderedDict.
- OrderedDict: preserves insertion order of keys.
- popitem(): removes and returns the last item by default, or the first item when last=False.
- move_to_end(): moves an existing key to either the end or the beginning.

### bisect_tree.py
This file shows how bisect helps with sorted lists.
- bisect.bisect_right(): finds the insertion point after existing values.
- bisect.bisect_left(): finds the insertion point before existing values.
- bisect.insort_left(): inserts an element while keeping the list sorted.
- bisect.insort_right(): inserts an element while keeping the list sorted after existing equal values.
- bisect.insort(): inserts an element using the appropriate insertion point.

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
Example: python3 DSA_Day_4/random_module.py

## Notes
The scripts are intended for learning and practicing core Python concepts alongside DSA topics.
