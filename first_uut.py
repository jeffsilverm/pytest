#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Unit Under Test

def add_2_always_right ( a:int, b:int ) -> int:
    """Add 2 integers and always return the correct answer """
    return a + b

def add_2_always_wrong ( a: int, b:int ) -> int:
    """Add 2 integers and never return the correct answer """
    return a + b - 1

def add_2_sometimes_wrong ( a: int, b: int) -> int:
    """Add 2 integers and usually return the correct answer"""
    s = a + b
    if s == 10:
        s = 11
    return s

def add_2_always_right_strongly_typed ( a: int, b: int) -> int:
    """Add 2 integers and always return the correct answer.  If passed something
     other than 2 integers, raise a ValueError exception"""

    if not isinstance(a, int):
        raise ValueError ( f"a is a {type(a)} but should be an int")
    if not isinstance(b, int):
        raise ValueError ( f"b is a {type(b)} but should be an int")
    return a + b

