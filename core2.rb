=begin
	
HTMLはDocument Object Model、
つまりDOMというのでデータが構造化されています。

今回の場合だと、2User以下のエントリだけを表示する
ということを考えています。
しかし、単純にUser数だけを数えても、
それは意味ないので、
ここで「必要な情報は何か」を考えます。
自分の場合は、以下のようになりました。

ページタイトル
ページのURL
User数
	
=end

require 'nokogiri'
require 'open-uri'

URL = 'http://b.hatena.ne.jp/entrylist?sort=hot&threshold=2'
html = open(URL) { |f| f.read }

doc = Nokogiri::HTML.parse(html, nil)

doc.css(".entry-unit").each do |entry|
  p entry.css('h3').text
  p entry.css('h3 a.entry-link')[0][:href]
  p entry.css('blockquote').text
  p entry['data-bookmark-count'].to_i 
end
