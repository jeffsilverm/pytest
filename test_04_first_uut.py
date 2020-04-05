#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from first_uut import *

# When pytest says it has collected 5 items, it is referring to the length of
# tst_case_list
tst_case_list = [(2, 2, 4), (2, 3, 5), (8, 2, 10), (-2, -2, -4), ("q", "r", "qr")]


@pytest.mark.parametrize("a,b,e", tst_case_list)
def test_first_uut(a, b, e):
    def test_add_2_always_right(a, b, e):
        assert add_2_always_right(a, b) == e

    @pytest.mark.xfail
    def test_add_2_always_wrong(a, b, e):
        assert add_2_always_wrong(a, b) == e

    def test_add_2_sometimes_wrong(a, b, e):
        assert add_2_sometimes_wrong(a, b) == e

    def test_add_2_always_right_strongly_typed(a, b, e):
        assert add_2_always_right_strongly_typed(a, b) == e

    test_add_2_always_right(a, b, e)
    test_add_2_sometimes_wrong(a, b, e)
    with pytest.raises(ValueError):
        test_add_2_always_right_strongly_typed(a, b, e)
    try:
        test_add_2_always_wrong(a, b, e)
    except TypeError as t:
        if isinstance(a, str) or isinstance(b, str):
            print("add_2_always_wrong raised a TypeError exception as it should",
                  file=sys.stderr)
        else:
            print("add_2_always_wrong raised a TypeError exception UNEXPECTEDLY",
                  file=sys.stderr)
            raise
    except Exception:
        raise
