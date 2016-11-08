import sys
import requests
import bs4 as bs

query = sys.argv[1].split()
ref = ' '.join(query[:-1])
version = ''

first_char_of_last_arg = query[-1].split(':')[-1][0]
if first_char_of_last_arg.isalpha():
    version = query[-1]
else:
    ref += ' ' + query[-1]

url = 'https://www.biblegateway.com/passage/?search={}&version={}'.format(ref,version)
res = requests.get(url)
soup = bs.BeautifulSoup(res.text, 'html.parser')

result = ''
for passage in soup.find_all('div', class_='passage-box'):

    passage_div = passage.find('div', 'passage-content').div
    for p in passage_div.find_all('p'):
        for unwanted in p.find_all('sup', ['footnote', 'crossreference', 'versenum']):
            unwanted.decompose()

        result += p.text + ' '

    clean_reference = passage_div.h1.span.text
    version = passage_div['class'][0].split('-')[-1]

    result += "\n{} {}\n\n".format(clean_reference, version)

print(result)


