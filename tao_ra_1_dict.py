# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:15:54 2024

@author: ADMIN
"""


n = int(input("Nhập giá trị nguyên n: "))

result_dict = {i: i ** i for i in range(1, n + 1)}

print(result_dict)
