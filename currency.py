import requests
from bs4 import BeautifulSoup


# url_usd = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=' \
#           '&aqs=chrome.0.35i39i362l8.281436867j0j15&sourceid=chrome&ie=UTF-8'
# url_eur = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=AOaemvLQc-UVRka' \
#           'A1kXHb3njULf9A7VaGA%3A1639053463315&ei=l_ixYe2BEoqdrgSZpq34BA&ved=0ahUKEwitqcr73db0AhWKjosKHRlTC08Q4dUD' \
#           'CA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQ' \
#           'ggIyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMgsIABC' \
#           'ABBCxAxDJAzIFCAAQkgM6BwgjELADECc6BwgAEEcQsAM6CggAEEcQsAMQyQM6CAgAEJIDELADOhAILhDHARDRAxDIAxCwAxBDOgQIIx' \
#           'AnOhAIABCABBCHAhCxAxCDARAUOgsIABCABBCxAxCDAToFCAAQgAQ6BwgjEOoCECc6CQgjECcQRhCCAjoNCAAQgAQQhwIQsQMQFDoOC' \
#           'C4QgAQQsQMQxwEQowI6BwgAELEDEEM6BAgAEEM6CggAELEDEIMBEENKBAhBGABKBAhGGABQvQxYxy9g0jdoBXACeAKAAWiIAcsIkgEE' \
#           'MTYuMZgBAKABAbABCsgBC8ABAQ&sclient=gws-wiz'
# url_btc = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%' \
#           'B0+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&sxsrf=AOaemvK2FOllxnvWWN-P38RKjtCoUTYS2g%3A1' \
#           '639080174438&ei=7mCyYeyyGanrrgTD0bzQDA&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8' \
#           '%D0%BD%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsAMQJzIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAA' \
#           'QRxCwAzIKCAAQRxCwAxDJAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQzIHCAAQsAMQQzIQCC4QxwEQ0QMQyAMQsA' \
#           'MQQzIQCC4QxwEQ0QMQyAMQsAMQQzIQCC4QxwEQ0QMQyAMQsAMQQzIQCC4QxwEQ0QMQyAMQsAMQQzIQCC4QxwEQowIQyAMQsAMQQ0oEC' \
#           'EEYAEoECEYYAVAAWABg7gVoAXACeACAAQCIAQCSAQCYAQDIARHAAQE&sclient=gws-wiz'
# url_eth = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8D%D1%84%D0%B8%D1%80%D0%B0+%D0%B2+%D0%B4%D' \
#           '0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&sxsrf=AOaemvIyu0dwvU0J0KTX1uMjQcMHikcUqw%3A1639080413626&ei=3W' \
#           'GyYayJJZaXrwTT0YaoCg&oq=%D0%BA%D1%83%D1%80%D1%81+%27ab+%D0%B2+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B' \
#           '0%D1%85&gs_lcp=Cgdnd3Mtd2l6EAMYADIECAAQDTIECAAQDTIECAAQDTIECAAQDTIICAAQCBANEB46BwgjELADECc6BwgAEEcQsAM6' \
#           'CggAEEcQsAMQyQM6BwgAELADEEM6EAguEMcBENEDEMgDELADEEM6EAguEMcBEKMCEMgDELADEEM6BggAEAcQHjoHCCMQsAIQJzoMCCM' \
#           'QsAIQJxBGEIICOgUIABCABEoECEEYAEoECEYYAVD6C1ibIWCAMmgBcAJ4AIABYYgBswaSAQIxMZgBAKABAcgBE8ABAQ&sclient=gws-wiz'
# headers = {
# }     # YOUR USER AGENT
#
#
# class Currency():
#     def __init__(self, name):
#         self.name = name
#
#     def get_value_cb(self, url, headers):
#         page = requests.get(url, headers=headers)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
#         return float((convert[0].text).replace(',', '.'))
#
#     def get_value_crypto(self, url, headers):
#         page = requests.get(url, headers=headers)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         convert = soup.findAll('span', {'class': 'pclqee'})
#         convert = ((convert[0].text).replace('\xa0', ''))
#         return (float(convert.replace(',', '.')))


url_usd = 'https://quote.rbc.ru/ticker/72413'
url_eur = 'https://quote.rbc.ru/ticker/59090'
url_btc = 'https://www.rbc.ru/crypto/currency/btcusd'
url_eth = 'https://www.rbc.ru/crypto/currency/ethusd'


class Currency():
    def __init__(self, name):
        self.name = name

    def get_currency(self, url):
        source = requests.get(url)
        main_text = source.text
        soup = BeautifulSoup(main_text, features='html.parser')
        wallet = soup.find('span', {'class': 'chart__info__sum'})
        wallet = wallet.text.replace('₽', '')
        wallet = float(wallet.replace(',', '.'))
        return wallet

    def get_crypto(self, url):
        source = requests.get(url)
        main_text = source.text
        soup = BeautifulSoup(main_text, features='html.parser')
        coin = soup.find('div', {'class': 'chart__subtitle js-chart-value'})
        coin = coin.text.replace(' ', '').split()
        coin = float(coin[0].replace(',', '.'))
        return coin
