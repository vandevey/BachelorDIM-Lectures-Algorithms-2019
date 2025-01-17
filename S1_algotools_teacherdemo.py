# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:18:46 2019

@author: vandevey
"""

# --- Premiers pas ---
'''
print('Galettes saucisses')

myVariable = 0

print('My variable = ', myVariable)

'''
# --- Algorithm 1 ---
'''
def mySum(param1, param2) : 

    Function that sums two input params int value
    
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

print('Sum function=', mySum(1,2))
'''

# --- Algorithm Averaging ---

tab = [12, 15, 8, 14, 13]

def average_above_zero(tab) :
    if not(isinstance(tab, list)) :
        raise ValueError('average_above_zero, expected a list as input')
    if (len(tab) == 0) :
        raise ValueError('average_above_zero, can\'t use an empty list as input')
    if not(isinstance(tab[0], (int, float))) :
        raise ValueError('average_above_zero, expected a list as input')
     
    pos_val_sum = 0
    nbr_element = 0
    moy = 0
    for id in range(len(tab)) :
        if tab[id] > 0 :
            nbr_element += 1
            pos_val_sum += tab[id]
            
    moy = pos_val_sum / nbr_element       
    return moy
    
print('Average above zero =', average_above_zero(tab))    

# --- Algorithm Max ---
    
tab = [12, 15, 8, 14, 18]

def max_value(tab) :
    if not(isinstance(tab, list)) :
        raise ValueError('max_value, expected a list as input')
    if (len(tab) == 0) :
        raise ValueError('max_value, can\'t use an empty list as input')
    if not(isinstance(tab[0], (int, float))) :
        raise ValueError('max_value, expected a list as input')
     
    max_val = 0
    for i in range(len(tab)) :
        if tab[i] > max_val :
            max_val = tab[i]
            
    return max_val
    
print('Valeur max =', max_value(tab))  

# --- Algorithm Reverse table ---  

tab = [12, 15, 8, 14, 18]

def reverse_tab(tab) :
    if not(isinstance(tab, list)) :
        raise ValueError('reverse_tab, expected a list as input')
    if (len(tab) == 0) :
        raise ValueError('reverse_tab, can\'t use an empty list as input')
    if not(isinstance(tab[0], (int, float))) :
        raise ValueError('reverse_tab, expected a list as input')
      
    tab.reverse()
        
    return tab
    
print('Tableaux inverser =', reverse_tab(tab))  

# --- Algorithm Bounding box ---  


# --- Algorithm Random array filling ---  

# --- Remove whitespace characters in a string  ---  

sentence = ' Le Python c\'est mieux que ce que je pensais'

def remove_whitespace(sentence) :
    if (len(sentence) == 0) :
        raise ValueError('remove_whitespace, can\'t use an empty string as input')
    if not(isinstance(tab[0], (int, float))) :
        raise ValueError('remove_whitespace, expected a string as input')
    new_sentence = 0
    new_sentence = sentence.replace(" ", "")
    return new_sentence

print('Sentence whithout spaces =', remove_whitespace(sentence))  







