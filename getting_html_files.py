import requests

# str/list of userAgent/s
userAgent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/130.0.0.0 Safari/537.3')

# url of a websites
url_moto = 'https://www.otomoto.pl/osobowe?search%5Border%5D=created_at%3Adesc'
url_dom = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/zachodniopomorskie/szczecin/szczecin/szczecin'

# checking response
response_moto = requests.get(url_moto, headers={'User-Agent': userAgent})
response_dom = requests.get(url_dom, headers={'User-Agent': userAgent})

print("Response from Otomoto: {}; response from Otodom: {}".format(response_moto, response_moto))

# getting html code
with open("Otomoto_HTML.html", 'w', encoding='utf-8') as file:
    file.write(response_moto.text)
with open("Otodom_HTML.html", 'w', encoding='utf-8') as file:
    file.write(response_dom.text)
