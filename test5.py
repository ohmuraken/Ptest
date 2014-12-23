page = web contents
"""
start_link = page.find("<a href=")
start_quote = page.find('"',start_link)
end_quote = pages.find('"',start_link+1)
url = pages[start_link+1:end_quote]
print url
"""
def get_next_target(page):
	start_link = page.find('<a href=')
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = pages[start_quote+1:end_quote]
	return url, end_quote

url, end_quote = get_next_target(page)


#a,b = 1,2
"""

>>> t=1
>>> s=2
>>> t,s=s,t
>>> t
2
>>> s
1


>>> t=1
>>> s=2
>>> t=s
>>> s=t
>>> t
2
>>> s
2
>>>
"""

