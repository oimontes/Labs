#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:17:34 2019

@author: Oscar Montes
"""

def find_file():
    access = open('words_alpha.txt')
    file1 = access.readlines()
    access.close()
    return file1

def fill_set(file1):
    alpha = {textLines.strip() for textLines in file1}
    return alpha

def find_anagram(user_input, access):
  
    return list2

print('Hello, please input a word,', end=' ')
print('or an empty space to finish:')
test_word = input()

file1 = find_file()
access = fill_set(file1)
all_anagram = find_anagram(test_word, access)
print (*sorted(all_anagram), sep = "\n")