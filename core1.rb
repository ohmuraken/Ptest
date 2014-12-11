=begin
はてなブックマークから
「2User以下のエントリだけを表示する」
というプログラムを書くとします。
このとき、まず最初に必要になるのは、
あるサイトにアクセスしてきて、
HTMLを引っ張ってくる部分です。
そこで、愚直にアクセスし、URLを確認し、
そのソースを表示するように作成してみます。
=end
rescue Exception => e
	
end

require 'open-uri'

URL = 'http://b.hatena.ne.jp/entrylist?sort=hot&threshold=2'
html = open(URL) { |f| f.read }
puts html
