#test14.py
#coding: UTF-8
"""
同じオブジェクトを参照する2つの異なる方法がある
エイリアシング

ジェームズボンドは
"ジェームズボンド"
と呼ぶし
"007"とも呼ぶみたいに
"""

p=["a","b", "c"]
q=p
q[0]="g"
print p
print q
"""
$python test14.py
['g', 'b', 'c']
['g', 'b', 'c']
"""