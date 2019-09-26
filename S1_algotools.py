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


