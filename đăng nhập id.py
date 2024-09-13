# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:02:47 2024

@author: ADMIN
"""

import re

def is_valid_id_user(user_id):
    """
    Kiểm tra tính hợp lệ của ID người dùng.
    """
   
    id_pattern = r'^[a-zA-Z0-9]{6,24}$'
    
    
    if re.match(id_pattern, user_id):
        return True
    else:
        return False

def is_valid_password(password):
    """
    Kiểm tra tính hợp lệ của mật khẩu.
    """
   
    min_length = 6
    max_length = 24
    
    
    if not (min_length <= len(password) <= max_length):
        return False
    
   
    lower_pattern = r'[a-z]'
    digit_pattern = r'[0-9]'
    upper_pattern = r'[A-Z]'
    special_pattern = r'[$#@]'
    
    
    if (re.search(lower_pattern, password) and
        re.search(digit_pattern, password) and
        re.search(upper_pattern, password) and
        re.search(special_pattern, password)):
        return True
    
    return False


def check_login(user_id, password):
    """
    Kiểm tra tính hợp lệ của ID người dùng và mật khẩu khi đăng nhập.
    """
    if is_valid_id_user(user_id) and is_valid_password(password):
        return "Đăng nhập thành công!"
    else:
        return "ID người dùng hoặc mật khẩu không hợp lệ."


print(check_login('user123', 'Password1$'))  
print(check_login('short', 'pass$123'))       
print(check_login('validUserID123', 'short')) 
print(check_login('userID1234', 'Passw0rd@')) 
print(check_login('validID', 'NoDigit@'))     
