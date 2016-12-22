import sys
import os
import re
import requests
import bs4 as bs

query = sys.argv[1].split()

first_char_of_last_arg = query[-1].split(':')[-1][0]
if first_char_of_last_arg.isalpha():  # version is included in query
    reference = ' '.join(query[:-1])
    version = query[-1]
else:
    reference = ' '.join(query)
    version = os.getenv('DEFAULT_BIBLE_VERSION', '')

url = 'https://www.biblegateway.com/passage/?search={}&version={}'.format(
      reference, version)

res = requests.get(url)
soup = bs.BeautifulSoup(res.text, 'html.parser')

result = ''
for passage in soup.find_all('div', class_='passage-box'):
    passage_div = passage.find('div', 'passage-content').div
    for p in passage_div.find_all('p'):
        for unwanted in p.find_all('br'):
            unwanted.replace_with(' ')
        for unwanted in p.find_all('sup', ['footnote',
                                           'crossreference',
                                           'versenum']):
            unwanted.decompose()
        result += re.sub('\s+', ' ', p.text) + ' '

    clean_reference = passage_div.h1.span.text
    version = passage_div['class'][0].split('-')[-1]

    result += "\n{} {}\n\n".format(clean_reference, version)

print(result.strip())
