#coding: UTF-8
def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()

	except:
	    return "error"

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link==-1:
		return None, 0;
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote 




def get_all_links(page):
	while True:
		url ,endpos = get_next_target(page)
		if url:
			print url
			page  = page[endpos:]
		else:
			break

#page = '<a href="result1">link1</a><a href="result2">link2</a><a href="result3">link3</a>'
print get_all_links(get_page('https://camph.net'))

#get_all_links(page)



