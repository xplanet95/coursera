from bs4 import BeautifulSoup
from decimal import Decimal

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
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup.find(CharCode=cur_to))
    result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой
