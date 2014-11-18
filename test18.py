#coding: UTF-8
#test18.py
#コマンドライン引数からURLを


#コマンドライン引数取得
import sys
if __name__ == "__main__":
    param = sys.argv
    print param
    page = param[1]

#get_pageを定義
def get_page(url):
	try:
	    import urllib
	    return urllib.urlopen(url).read()

	except:
	    return "error"

#ターゲットを変えていく
def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link==-1:
		return None, 0;
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote 

#リンク抽出
def get_all_links(page):
	while True:
		url ,endpos = get_next_target(page)
		if url:
			print url
			page  = page[endpos:]
		else:
			break

#ページの要素を全て取得
print get_page(page)

print ("==================")

#リンクのみを抽出
print get_all_links(get_page(page))