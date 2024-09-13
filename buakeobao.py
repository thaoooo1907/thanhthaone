# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:08:32 2024

@author: ADMIN
"""

import random

def get_computer_choice():
    """
    Chọn ngẫu nhiên một trong ba tùy chọn cho máy tính.
    """
    choices = ['Kéo', 'Búa', 'Bao']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Xác định người chiến thắng dựa trên các lựa chọn của người chơi và máy tính.
    """
    if user_choice == computer_choice:
        return 'Hòa!'
    
    if (user_choice == 'Kéo' and computer_choice == 'Bao') or \
       (user_choice == 'Búa' and computer_choice == 'Kéo') or \
       (user_choice == 'Bao' and computer_choice == 'Búa'):
        return 'Bạn thắng!'
    
    return 'Máy tính thắng!'

def play_game():
    """
    Chơi trò chơi Kéo - Búa - Bao.
    """
    print("Chào mừng đến với trò chơi Kéo - Búa - Bao!")
    print("Lựa chọn của bạn: Kéo, Búa, Bao")

    user_choice = input("Nhập lựa chọn của bạn: ").strip().capitalize()
    valid_choices = ['Kéo', 'Búa', 'Bao']
    
    if user_choice not in valid_choices:
        print("Lựa chọn không hợp lệ. Vui lòng chọn Kéo, Búa hoặc Bao.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Máy tính chọn: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
