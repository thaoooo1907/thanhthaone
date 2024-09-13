# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:00:25 2024

@author: Student
"""


so_chan = [so for so in range(2020, 3839) if so % 2 == 0]


so_chia_het_9 = [so for so in so_chan if so % 9 == 0]

print("\t".join(map(str, so_chia_het_9)))
