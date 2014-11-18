#coding: UTF-8
#test13.py
p = ["h","e","l","l","o"]
p[0] = "y"

#pとqは同じ所を参照しているぞ
q = p
q[4] = "!"

print p
print q
"""
['y', 'e', 'l', 'l', '!']
['y', 'e', 'l', 'l', '!']
"""

