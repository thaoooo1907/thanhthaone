# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:49:40 2024

@author: ADMIN
"""

import string

def analyze_string(s):
    
    length = len(s)
    print(f"Độ dài chuỗi: {length}")

   
    special_chars_count = 0
    alphabet_lower_count = 0
    digits_count = 0
    alphabet_upper_count = 0
    special_chars = "!@#$%^&*()-=+./"

   
    for char in s:
        if char in special_chars:
            special_chars_count += 1
        elif char in string.ascii_lowercase:
            alphabet_lower_count += 1
        elif char in string.digits:
            digits_count += 1
        elif char in string.ascii_uppercase:
            alphabet_upper_count += 1

  
    print(f"Số lượng ký tự đặc biệt: {special_chars_count}")
    print(f"Số lượng ký tự chữ cái từ [a-z]: {alphabet_lower_count}")
    print(f"Số lượng ký tự chữ số từ [0-9]: {digits_count}")
    print(f"Số lượng ký tự chữ cái từ [A-Z]: {alphabet_upper_count}")

def main():
   
    str_input = input("Nhập chuỗi: ")
    
   
    analyze_string(str_input)

if __name__ == "__main__":
    main()
