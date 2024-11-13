from bs4 import BeautifulSoup

# getting a data
with open("Otomoto_HTML.html", encoding='utf-8') as file:
    src = file.read()  # it's a first page

# making a soup
soup = BeautifulSoup(src, 'lxml')

# getting a list with pages links
list_of_links = []

link = 'https://www.otomoto.pl/osobowe/szczecin?search%5Bdist%5D=50&search%5Border%5D=created_at%3Adesc&page='

last_page_cont = soup.find_all('a', {'class': 'ooa-g4wbjr e1y5xfcl0'})[3]
last_page = int(last_page_cont.find('span').text)

for el in range(1, last_page + 1):
    list_of_links.append(link + f'{el}')

print(list_of_links[0:3])
