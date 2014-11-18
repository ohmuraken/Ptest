#coding: UTF-8
"""
replace_spy
input 3 list
３番目の要素を1増やす
"""

def replace_spy(spy):
	print spy
	#re_spy = spy
	spy[2]=spy[2]+1
	#re_spy[2]=re_spy[2]+1
	#return re_spy

spy=[0,0,7]
#print replace_spy(spy)
replace_spy(spy)
print spy