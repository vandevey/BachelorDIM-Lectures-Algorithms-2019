#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:44:54 2019

@author: alben
"""

import S1_algotools as test_s1

import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
'''        
def inc_(x):
    return x+1
'''
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0
        
# --- Average test ---
        
tab_list=[5,6,7,13,14,15]       
        
def test_average_correct():
    assert test_s1.average_above_zero(tab_list) == 10