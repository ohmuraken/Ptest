#coding: UTF-8
"""
あ
#coding: UTF-8
で文字指定しないとおこ
"""
def factorial(n):
	all = 1
	while n >=1:
		all = all*n
		n = n-1
	return all
	
print factorial(4)