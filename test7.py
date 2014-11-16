#coding: UTF-8
pages = 'this is a <a href="http://udacity.com">link!</a>'

def get_next_target(page):
	start_link = page.find('<a href=')
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = pages[start_quote+1:end_quote]
	return url, end_quote 

#url, end_quote = get_next_target(page)

url, endops = get_next_target(pages)
print url

#試しにURLが含まれないようなものをpagesとして渡す
pages = "good"
url, endops = get_next_target(pages)
print url
#出力は
#goo
"""
findは見つけられないと-1を返すので
goodの最後の文字の直前までの文字列を返す
"""


pages = 'Not "good" at all!'
url, endops = get_next_target(pages)
print url


"""




"""





