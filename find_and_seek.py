#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:20:41 2019
@author: Ivan Montes
"""
def select_bubble(L,k):
    check_array = False
    while (check_array == False):
        check_array = True
        x = 0
        while x < (len(L) - 1):
            if(L[x] > L[x+1]):    
                check_array = False
                hold = L[x]
                L[x] = L[x+1]
                L[x+1] = hold
            x = x + 1
    k = L[k]
    return k

L = [100, 5, 80, 69, 20]
print('Hi, please pick a number between 0 and', len(L) - 1, end=': ')
value = int(input())
print(L)
k = select_bubble(L, value)        
print(L)
print('Element',value,'in the list is: ', k)
#-------------------------------------------------------------------------
#select_bubble(L,0)
#print(L[0])
#for x in test_list: