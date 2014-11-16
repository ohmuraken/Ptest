#coding: UTF-8
#修正版
pages = 'this is a <a href="http://udacity.com">link!</a>'

def get_next_target(page):
	start_link = page.find('<a href=')
	if(start_link==-1):
		return None, 0;
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = pages[start_quote+1:end_quote]
	return url, end_quote 

#url, endops = get_next_target('Not "good"')
url, endops = get_next_target(pages)

#Noneは文字列みなやつだがFalseと同じ扱いができる
if url:
	print "Here!"
else:
	print "Not Here"


