# -*- coding: utf-8 -*-
import urllib
from urlparse import urljoin


def get_page(url):
	try:
	    return urllib.urlopen(url).read()

	except:
	    return "IOerror"


def get_next_target(page, startpos):
	start_link = page.find('<a href=', startpos)
	if start_link == -1:
		return None, 0;
	
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote 


def print_all_links(basic_url, page):
	print basic_url
	startpos = 0
	while 1:
		##returnでふたつ返す
		url, startpos = get_next_target(page, startpos)
		
		if url is None:
			break

		print urljoin(basic_url, url)
		#page = page[endpos:]
		#メモリをコピーではなく切り取りをかえる

url = 'https://camph.net'
html = get_page(url)
print html
print ("==================")
print_all_links(url, html)