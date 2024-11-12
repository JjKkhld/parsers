from bs4 import BeautifulSoup

# getting a data
with open("Otomoto_HTML.html", encoding='utf-8') as file:
    src = file.read()

# making a soup
soup = BeautifulSoup(src, 'lxml')

# define pages container
container_pages = soup.find('ul', {'class': 'pagination-list ooa-1vdlgt7'})
print(container_pages.find('li', {'class': 'pagination-item ooa-jolj3n'}))