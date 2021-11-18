from bs4 import BeautifulSoup as bs
import unittest
import os



def parse(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as html:
        soup = bs(html, 'lxml')
        print([soup.a.next for i in soup])

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    # unittest.main()
    for filename in os.listdir('wiki'):
        path = f'wiki/{filename}'
        parse(path)