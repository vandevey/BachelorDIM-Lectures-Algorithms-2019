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
   
# --- Average test ---
        
     
        
def test_average_working():
    tab_list=[5,6,7,13,14,15]  
    test, lastID = test_s1.average_above_zero(tab_list)
    assert test == 10