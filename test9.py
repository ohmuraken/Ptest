#coding: UTF-8
def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link==-1:
		return None, 0;
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = pages[start_quote+1:end_quote]
	return url, end_quote 



def get_all_links(pages):
	while True:
		url ,endpos = get_next_target(page)
		if url:
			print url
			page  = page[endpos:]
		else:
			break

page = '<a href="result1">link1</a><a href="result2">link2</a><a href="result3">link3</a>'

get_all_links(page)



