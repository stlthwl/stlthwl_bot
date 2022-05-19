import requests
from bs4 import BeautifulSoup


# headers = {
# }     # YOUR USER AGENT
# url_news = 'https://yandex.ru/'
#
#
# class News():
#     def __init__(self, newsline):
#         self.newsline = newsline
#
#     def get_newsline(self, url, headers):
#         page = requests.get(url, headers=headers)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         convert = soup.findAll('span', {'class': 'news__item-content'})
#         lst = []
#         for i in convert:
#             lst.append(i.text.replace('\xa0', ' '))
#         news_1 = lst[0]
#         news_2 = lst[1]
#         news_3 = lst[3]
#         news_4 = lst[4]
#         return str(f'Сейчвс в СМИ:\n\n- {news_1}.\n\n- {news_2}.\n\n- {news_3}.\n\n- {news_4}.')


url_news = 'https://lenta.ru/'


# class News():
#     def __init__(self, news_line):
#         self.news_line = news_line
#
#     def get_news_line(self, url):
#         source = requests.get(url)
#         main_text = source.text
#         soup = BeautifulSoup(main_text)
#         news = soup.findAll('span', {'class': 'news__item-content'})
#         lst = []
#         for i in news:
#             lst.append(i.text)
#         return (f'Сейчас в СМИ:\n\n- {lst[0]}.\n\n- {lst[1]}.\n\n- {lst[2]}.\n\n- {lst[3]}.')
class News():
    def __init__(self, news_line):
        self.news_line = news_line

    def get_news_line(self, url):
        source = requests.get(url)
        main_text = source.text
        soup = BeautifulSoup(main_text, features='html.parser')
        news = soup.findAll('span', {'class': 'card-mini__title'})
        lst = []
        for i in news:
            lst.append(i.text)
        return (f'Сейчас в СМИ:\n\n- {lst[0]}.\n\n- {lst[1]}.\n\n- {lst[2]}.\n\n- {lst[3]}.'
                f'\n\n- {lst[4]}.\n\n- {lst[5]}.')
