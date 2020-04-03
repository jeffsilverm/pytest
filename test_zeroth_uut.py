#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from zeroth_uut import *

def test_add_2_always_right():
    assert add_2_always_right(2, 2) == 4
    pass

def test_add_2_always_wrong ():
    assert add_2_always_wrong(2, 2) == 4
    pass

def test_add_2_sometimes_wrong():
    assert add_2_sometimes_wrong(2, 2) == 4
    pass

def test_add_2_always_right_strongly_typed():
    assert add_2_always_right_strongly_typed(2, 2) == 4
    pass


