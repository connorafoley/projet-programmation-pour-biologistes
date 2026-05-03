# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 10:02:21 2026

@author: conno
"""

#!/usr/bin/env puthon3
import my_functions

def main():
    print('Hello, World!')
    inputname = input("What is your name? ")
    my_functions.greeting(inputname)

'''
set env for this script; is it main(), or is this a module being called by something else?
'''

if __name__ == '__main__':
    main()
    