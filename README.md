# Code Tutorial

This is a very basic repository demonstrating how to structure a very basic
Python package.

## Contents

The repository contains:

- an example script (`script.py`) that is executable and which imports the package library,
- a single Python package module (`package`), which contains:
    - a library module (`lib.py`) and
    - a unit testing module (`tests.py`).

### Library

The library module contains a series of unitary functions for converting units and
calculating angular separation.

### Unit Tests

The unit testing module tests all of the functions in the library module.

### Package

The package hosts the library and its unit tests.

### Script

The script imports the package library to perform a specific task, in this case
calculating the angular separation between two well known stars.

## Execution

The script can be executed simply by running:

```bash
$ ./script.py
```

The unit tests can be executed by running:

```bash
$ python package/tests.py -v
```
