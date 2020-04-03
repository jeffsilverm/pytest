#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Unit Under Test

def add_2_always_right ( a:int, b:int ) -> int:
    """Add 2 integers and always return the correct answer """
    pass

def add_2_always_wrong ( a: int, b:int ) -> int:
    """Add 2 integers and never return the correct answer """
    pass

def add_2_sometimes_wrong ( a: int, b: int) -> int:
    """Add 2 integers and usually return the correct answer"""
    pass

def add_2_always_right_strongly_typed ( a: int, b: int) -> int:
    """Add 2 integers and always return the correct answer.  If passed something
     other than 2 integers, raise a ValueError exception"""
    pass


