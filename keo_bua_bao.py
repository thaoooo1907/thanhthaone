# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:27:12 2024

@author: ADMIN
"""

import random

def get_computer_choice():
    choices = ['Kéo', 'Búa', 'Bao']
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "Hòa"
    elif (player == 'Kéo' and computer == 'Bao') or \
         (player == 'Búa' and computer == 'Kéo') or \
         (player == 'Bao' and computer == 'Búa'):
        return "Bạn thắng!"
    else:
        return "Máy thắng!"


def play_game():
    print("Chào mừng đến với trò chơi Kéo - Búa - Bao!")
    choices = ['Kéo', 'Búa', 'Bao']
    
    while True:
       
        player_choice = input("Nhập lựa chọn của bạn (Kéo/Búa/Bao) hoặc 'dừng' để kết thúc trò chơi: ").capitalize()
        
        if player_choice.lower() == 'dừng':
            print("Cảm ơn bạn đã chơi!")
            break
        
        if player_choice not in choices:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
        computer_choice = get_computer_choice()
        print(f"Máy chọn: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        print()
play_game()
