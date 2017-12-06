#!/usr/bin/env python
# Simple Daikon-style invariant checker
# Andreas Zeller, May 2012
# Complete the provided code, using your code from
# first exercise and adding ability to infer assertions
# for variable type, set and relations
# Modify only the classes Range and Invariants,
# if you need additional functions, make sure
# they are inside the classes.

import sys
import math
import random


def square_root(x, eps=0.00001):
    assert x >= 0
    y = math.sqrt(x)
    assert abs(square(y) - x) <= eps
    return y


def square(x):
    return x * x


def double(x):
    return abs(20 * x) + 10


# The Range class tracks the types and value ranges for a single variable.
class Range:
    def __init__(self):
        self.min = None  # Minimum value seen
        self.max = None  # Maximum value seen
        self.type = None  # Type of variable
        self.set = set()  # Set of values taken

    # Invoke this for every value
    def track(self, value):
        pass

    # YOUR CODE

    def __repr__(self):
        repr(self.type) + " " + repr(self.min) + ".." + repr(self.max) + " " + repr(self.set)


# The Invariants class tracks all Ranges for all variables seen.
class Invariants:
    def __init__(self):
        # Mapping (Function Name) -> (Event type) -> (Variable Name)
        # e.g. self.vars["sqrt"]["call"]["x"] = Range()
        # holds the range for the argument x when calling sqrt(x)
        self.vars = {}

    def track(self, frame, event, arg):
        if event == "call" or event == "return":
            pass
    # MAKE SURE TO TRACK ALL VARIABLES AND THEIR VALUES

    def __repr__(self):
        # Return the tracked invariants
        s = ""
        for function, events in self.vars.iteritems():
            for event, vars in events.iteritems():
                s += event + " " + function + ":\n"

                for var, range in vars.iteritems():
                    s += "    assert isinstance(" + var +  # YOUR CODE
                    s += "    assert "
                    if range.min == range.max:
                        s += var + " == " + repr(range.min)
                    else:
                        s += repr(range.min) + " <= " + var + " <= " + repr(range.max)
                    s += "\n"
                    # ADD HERE RELATIONS BETWEEN VARIABLES
                    # RELATIONS SHOULD BE ONE OF: ==, <=, >=
                    s += "    assert " + var + " >= " + var2 + "\n"
        return s


invariants = Invariants()


def traceit(frame, event, arg):
    invariants.track(frame, event, arg)
    return traceit


sys.settrace(traceit)
# Tester. Increase the range for more precise results when running locally
eps = 0.000001
test_vars = [34.6363, 9.348, -293438.402]
for i in test_vars:
    # for i in range(1, 10):
    z = double(i)
sys.settrace(None)
print invariants

# Example sample of a correct output:
"""
return double:
    assert isinstance(x, type(-293438.402))
    assert x in set([9.348, -293438.402, 34.6363])
    assert -293438.402 <= x <= 34.6363
    assert x <= ret
"""
