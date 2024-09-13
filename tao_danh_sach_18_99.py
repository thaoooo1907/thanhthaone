# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:30:27 2024

@author: Student
"""

import random

so_luong_phan_tu = random.randint(20, 30)


danh_sach_binh_phuong = []

for _ in range(so_luong_phan_tu):
    so_thuc = random.uniform(18, 99) 
    binh_phuong = so_thuc ** 2        
    danh_sach_binh_phuong.append(binh_phuong) 

print("Danh sách các giá trị bình phương:")
print(danh_sach_binh_phuong)
