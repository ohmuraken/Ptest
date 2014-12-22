# -*- coding: utf-8 -*-
import urllib
from urlparse import urljoin


def get_page(url):
	try:
	    return urllib.urlopen(url).read()

	except:
	    return "IOerror"


def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0;
	
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote 


def print_all_links(basic_url, page):
	print basic_url
	while 1:
		##returnでふたつ返す
		url, endpos = get_next_target(page)
		
		if url is None:
			break

		print urljoin(basic_url, url)
		page = page[endpos:]
		#メモリをコピーではなく切り取りをかえる


#page = '<a href="result1">link1</a><a href="result2">link2</a><a href="result3">link3</a>'
url = 'https://camph.net'
html = get_page(url)
print html
print ("==================")
print_all_links(url, html)

#get_all_links(page)