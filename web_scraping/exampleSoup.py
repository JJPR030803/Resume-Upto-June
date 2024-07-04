import requests,bs4

res = requests.get('https://www.amazon.com.mx/?tag=admarketdskmx-20&ref=pd_sl_4b9051fbecd3d82ebf7e046a2d6aea255c61b44bde0b7ef71a5283d4&mfadid=adm')
res.raise_for_status()
examopleSoup = bs4.BeautifulSoup(res.text,'html.parser')
elems = examopleSoup.select('#author')
print(type(elems))