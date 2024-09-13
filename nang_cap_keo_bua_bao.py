# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:33:06 2024

@author: ADMIN
"""

import random
choices = ['Kéo', 'Búa', 'Bao']
def get_random_choice():
    return random.choice(choices)
def determine_winner(player1, player2):
    if player1 == player2:
        return (0, 0)  # Hòa
    elif (player1 == 'Kéo' and player2 == 'Bao') or \
         (player1 == 'Búa' and player2 == 'Kéo') or \
         (player1 == 'Bao' and player2 == 'Búa'):
        return (1, 0)  
    else:
        return (0, 1)  
def play_game():
    num_players = random.randint(8, 20)  # Chọn ngẫu nhiên số lượng người chơi từ 8 đến 20
    print(f"Số lượng người chơi: {num_players}")
    choices_list = [get_random_choice() for _ in range(num_players)]
    scores = [0] * num_players
    for i in range(num_players):
        for j in range(i + 1, num_players):
            result = determine_winner(choices_list[i], choices_list[j])
            if result[0] > result[1]:
                scores[i] += 1
            elif result[1] > result[0]:
                scores[j] += 1
    for i in range(num_players):
        print(f"Người chơi {i + 1}: Lựa chọn = {choices_list[i]}, Điểm = {scores[i]}")
    max_score = max(scores)
    winners = [i + 1 for i in range(num_players) if scores[i] == max_score]
    
    print(f"Người thắng cuộc: Người chơi {', '.join(map(str, winners))} với {max_score} điểm!")
play_game()
