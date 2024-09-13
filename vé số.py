# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:10:05 2024

@author: ADMIN
"""

import random

def generate_random_numbers():
    """
    Tạo một dãy số ngẫu nhiên gồm 6 số không trùng nhau từ 1 đến 45.
    """
    return sorted(random.sample(range(1, 46), 6))

def calculate_prize(matched_count):
    """
    Tính toán số tiền thưởng dựa trên số lượng số trùng khớp.
    """
    if matched_count == 6:
        return 10_000_000_000  
    elif matched_count == 5:
        return 10_000_000  
    elif matched_count == 4:
        return 300_000 
    elif matched_count == 3:
        return 30_000  
    else:
        return 0

def check_results(ticket_numbers, winning_numbers):
    """
    So sánh dãy số của vé và dãy số trúng thưởng để tính số lượng số trùng khớp.
    """
    matched_count = len(set(ticket_numbers) & set(winning_numbers))
    return matched_count

def main():
    
    num_tickets = int(input("Nhập số lượng vé số bạn muốn mua: "))
    
    
    winning_numbers = generate_random_numbers()
    print(f"Dãy số trúng thưởng: {winning_numbers}")
    
    
    tickets = []
    for i in range(num_tickets):
        ticket_numbers = generate_random_numbers()
        tickets.append(ticket_numbers)
        print(f"Vé số {i+1}: {ticket_numbers}")
    
    
    ticket_price = 10_000  
    
    
    total_prize = 0
    for i, ticket in enumerate(tickets):
        matched_count = check_results(ticket, winning_numbers)
        prize = calculate_prize(matched_count)
        total_prize += prize
        print(f"Vé số {i+1} trúng {matched_count} số. Thưởng: {prize} đồng.")
    
   
    print(f"Tổng tiền thưởng nhận được: {total_prize} đồng.")

if __name__ == "__main__":
    main()
