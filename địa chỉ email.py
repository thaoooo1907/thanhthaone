# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:05:14 2024

@author: ADMIN
"""

import re


valid_domains = {
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "aol.com",
    "zoho.com",
    "protonmail.com"
}

def is_valid_email(email):
    """
    Kiểm tra xem địa chỉ email có hợp lệ không.
    """
    
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        return False

   
    try:
        username, domain = email.split('@')
    except ValueError:
        return False

    
    if domain not in valid_domains:
        return False

   
    if len(username) < 6 or not username.isalnum():
        return False

    return True

def main():
    
    email = input("Nhập địa chỉ email: ")
    
   
    if is_valid_email(email):
        print("Địa chỉ email hợp lệ.")
    else:
        print("Địa chỉ email không hợp lệ.")

if __name__ == "__main__":
    main()
