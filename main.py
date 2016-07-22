import requests
from bs4 import BeautifulSoup


def main():
    get_regions()


def get_regions():
    with requests.Session() as ace:
        url = 'http://kolesa.kz'
        page = ace.get(url)
        print(page.text)

if __name__ == '__main__':
    main()