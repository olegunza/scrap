import requests
from bs4 import BeautifulSoup


def main():
    get_pages()


def get_pages():
    with requests.Session() as ace:
        url = 'http://kolesa.kz/cars/'
        page = ace.get(url)
        bs_page = BeautifulSoup(page.text, 'lxml')
        last_page = bs_page.find('div', {'class': 'pager'})
        print(last_page)

if __name__ == '__main__':
    main()