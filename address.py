from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://shikiho.jp/')
r.html.render() # サイトを描画させる

hoge_class = r.html.find('.hoge') # hoge クラスのデータを取得