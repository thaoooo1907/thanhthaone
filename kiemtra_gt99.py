# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:51:10 2024

@author: Student
"""

x = float(input("nhập số:"))
while x > -99 or x < 99:
    x = float(input(" nhập lại số: "))
    print ("giá trị đã nhập:", x)
    