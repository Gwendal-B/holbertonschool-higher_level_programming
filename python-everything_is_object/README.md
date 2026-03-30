
# Everything is an Object

## Background Context

This project explores how Python handles objects, references, and variable assignment. A key concept to understand is the difference between immutable and mutable types:

```python
# Immutable - creates new object
a = 1
b = a
a = 2
# b remains 1

# Mutable - references same object
l = [1, 2, 3]
m = l
l[0] = 'x'
# m is now ['x', 2, 3]
```

## Approach

Read the documentation, think critically, and brainstorm before testing in the interpreter. These concepts frequently appear in Python interviews.

## Learning Objectives

- Understand objects, classes, and instances
- Distinguish between immutable and mutable types
- Grasp references, assignments, and aliases
- Use `id()` to check variable identity
- Know built-in mutable types: lists, dictionaries, sets
- Know built-in immutable types: tuples, strings, numbers
- Understand how Python passes variables to functions

## Resources

- 9.10. Objects and values
- 9.11. Aliasing
- Immutable vs mutable types
- 9.12. Cloning lists
- Python tuples: immutable but potentially changing

## Requirements

- Python 3.8.5 on Ubuntu 20.04 LTS
- All files executable with `#!/usr/bin/python3` shebang
- Comply with pycodestyle (2.7.*)
- Answer files contain only one line with no leading/trailing spaces
