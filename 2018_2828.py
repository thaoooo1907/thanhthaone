# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:57:30 2024

@author: Student
"""


danh_sach = []
for so in range(2018, 2829):
    
     if so % 2 == 0 and so % 5 == 0:
        danh_sach.append(so)

print("Danh sách các số chẵn chia hết cho 5 từ 2018 đến 2828:")
print(danh_sach)
