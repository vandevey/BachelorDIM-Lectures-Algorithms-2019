# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:18:46 2019

@author: vandevey
"""

# --- Premiers pas ---

print('Galettes saucisses')

myVariable = 0

print('My variable = ', myVariable)

# --- Algorithm 1 ---

def mySum(param1, param2) : 
    '''
    Function that sums two input params (int value)
    
    '''
    return param1 + param2


import numpy as np

tab_list=[1,2,3,4,5,6,7]

tab_zeros = np.zeros(12,dtype = np.int32)
tab_from_list = np.array(tab_list)

for id in range(len(tab_from_list)) :
    print('tab['+str(id)+'] = '+str(tab_from_list[id]))
    print('tab[{index}] = (val) '.format(index = id, val = tab_from_list[id]))
    
    if tab_from_list[id] > 0 :
        print('Yessaï')
        
print('Finished')

print('sum function=', mySum(1,2))

# --- Algorithm Averaging ---

tab = [12, 15, 8, 14, 13]

def average_above_zero(tab) :
    pos_val_sum = 0
    nbr_element = 0
    moy = 0
    for id in range(len(tab)) :
        if tab[id] > 0 :
            nbr_element += 1
            pos_val_sum += tab[id]
            
    moy = pos_val_sum / nbr_element       
    return moy
    
print('sum function=', average_above_zero(tab))    

# --- Algorithm Max ---
    
tab = [12, 15, 8, 14, 18]

def max_value(tab) :
    max_val = 0
    
    for i in range(len(tab)) :
        if tab[i] > max_val :
            max_val = tab[i]
            
    return max_val
    
print('sum function=', max_value(tab))  

# --- Algorithm Reverse table ---  

tab = [12, 15, 8, 14, 18]

def reverse_tab(tab) :
    
    tab = tab.reverse
        
    return tab
    
print('sum function=', reverse_tab(tab))  


