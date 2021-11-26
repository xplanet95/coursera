from bs4 import BeautifulSoup as bs
import unittest
import os
import re



def parse(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as html:
        soup = bs(html, 'lxml')
        body = soup.find(id="bodyContent")

        imgs = len(body.find_all('img',  width=lambda x: int(x or 0) > 199))
        pattern = re.compile(r'[hH1-6]{2}')
        headers = len([i.text for i in body.find_all(name=pattern) if i.text[0] in 'ETC'])

        all_links = body.find_all('a')
        linkslen = 0
        for link in all_links:
            local_linkslen = 1
            for i in link.find_next_siblings():
                if i.name != 'a':
                    break
                local_linkslen += 1
            linkslen = max(linkslen, local_linkslen)

        lists = 0
        html_lists = body.find_all(['ul', 'ol'])
        for html_list in html_lists:
            if not html_list.find_parents(['ul', 'ol']):
                lists += 1
    print([imgs, headers, linkslen, lists])
    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),
            ('wiki/Stone_Age', [13, 10, 12, 40]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    # unittest.main()
    for filename in os.listdir('wiki'):
        path = f'wiki/{filename}'
        parse(path)