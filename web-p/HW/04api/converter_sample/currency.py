from bs4 import BeautifulSoup
from decimal import Decimal
import xml.etree.ElementTree as ET

# url = 'http://www.cbr.ru/scripts/XML_daily.asp'
# # params = {
# #     'date_req': date
# # }
# html = requests.get(url)
# soup = bs(html.content, 'lxml')
#
# print(soup.find())


#
def convert(amount, cur_from, cur_to, date, requests):
    result = 0
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    params = {
        'date_req': date,
    }
    response = requests.get(url, params)  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'lxml')
    valutes = soup.find_all('valute')
    name_of_valutes = []
    for i in valutes:
        name_valute = i.find('charcode').text
        name_of_valutes.append(name_valute)
        if name_valute == cur_to:
            value_of_valute_cur_to = Decimal(i.find('value').text.replace(',', '.'))
        if name_valute == cur_from:
            value_of_valute_cur_from = Decimal(i.find('value').text.replace(',', '.'))

    if cur_from in name_of_valutes:
        result = (value_of_valute_cur_from * amount / value_of_valute_cur_to * 100).quantize(Decimal('1.0000'))
    else:
        result = (amount / value_of_valute_cur_to * 100).quantize(Decimal('1.0000'))

    return result  # не забыть про округление до 4х знаков после запятой
