# search_string上にある2つ目のtaret_stringの位置を出力
#def find_second(search_string,target_string):
#	first = search_string.find("target_string")
#	second = setach.find(target_string,first+1)
#	return second

def isfriend(name):
	return name[0] == "D" or name[0] == "N"

print isfriend("David")
print isfriend("Tom")
print isfriend("Nancy")

#True or　は前をみて、False orは後ろをみる
print True or False
print False or True
print True or True
print False or False
print True or thisError
print False or thisError

def bigger(a,b):
	if a>b:
		r = a
	else:
		r =	b
	return r

def biggest(a,b,c):
	return bigger(a,bigger(b,c))

print biggest(1,2,3)
	



