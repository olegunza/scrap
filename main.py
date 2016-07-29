import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
GLOBAL_HEADERS = {'User-Agent': USER_AGENT, 'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-encoding': 'gzip, deflate', 'Connection': 'keep-alive',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}


def main():
    #get_last_page()
    get_links()


def get_last_page():
    with requests.Session() as ace:
        url = 'http://kolesa.kz'
        url_prefix = '/cars/'
        page = ace.get(url+url_prefix, headers=GLOBAL_HEADERS)
        bs_page = BeautifulSoup(page.text, 'lxml')
        pages = bs_page.find('div', {'class': 'pager'}).find_all('a')
        page_nums = [(''.join(num for num in page if num.isdigit())) for page in pages]
        last_page = max([int(num) for num in page_nums if num.isdigit()])
        return last_page


def get_links():
    with requests.Session() as ace:
        for i in range(1,3):
            url = 'http://kolesa.kz'
            url_prefix = '/cars/'
            get_url = url + url_prefix + '?page='+str(i)
            page = ace.get(get_url, headers=GLOBAL_HEADERS)
            bs_page = BeautifulSoup(page.text, 'lxml')
            pages = bs_page.find_all('div', {'class': 'list-title'})
            #links = [url + x["href"] for x in pages]
            print(pages)


if __name__ == '__main__':
    main()
