from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    result = 0
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url, {'date_req': date})  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'lxml')
    valutes = soup.find_all('valute')
    names_of_valute = []
    for i in valutes:
        name_valute = i.find('charcode').text
        names_of_valute.append(name_valute)
        if name_valute == cur_to:
            value_of_valute_cur_to = Decimal(i.find('value').text.replace(',', '.'))
        if name_valute == cur_from:
            value_of_valute_cur_from = Decimal(i.find('value').text.replace(',', '.'))

    if cur_from in names_of_valute:
        result = (value_of_valute_cur_from * amount / value_of_valute_cur_to * 100).quantize(Decimal('1.0000'))
    else:
        result = (amount / value_of_valute_cur_to * 100).quantize(Decimal('1.0000'))

    return result  # не забыть про округление до 4х знаков после запятой
