#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from first_uut import *

tst_case_list = [(2, 2, 4), (2, 3, 5), (8, 2, 10), ("q", "r", "qr")]


@pytest.mark.parametrize("a,b,e", tst_case_list)
def test_add_2_always_right(a, b, e):
    assert add_2_always_right(a, b) == e


@pytest.mark.parametrize("a,b,e", tst_case_list)
def test_add_2_always_wrong(a, b, e):
    assert add_2_always_wrong(a, b) == e


@pytest.mark.parametrize("a,b,e", tst_case_list)
def test_add_2_sometimes_wrong(a, b, e):
    assert add_2_sometimes_wrong(a, b) == e


@pytest.mark.parametrize("a,b,e", tst_case_list)
def test_add_2_always_right_strongly_typed(a, b, e):
    assert add_2_always_right_strongly_typed(a, b) == e
