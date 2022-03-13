import requests
from bs4 import BeautifulSoup
import lxml

AMAZON_URL = 'https://www.amazon.com/Magic-Gathering-Innistrad-Commander-Bloodline/dp/B099YJBTNF/'\
    'ref=sr_1_3?crid=382YCNUGBQ5D&keywords=mtg%2Bcommander%2Bdeck&qid=1647208996&'\
    'sprefix=mtg%2Bcommander%2Bdeck%2Caps%2C189&sr=8-3&th=1'

header = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0',
    "Accept-Language": 'en-US'
}

response = requests.get(url=AMAZON_URL, headers=header)
website = response.text

soup = BeautifulSoup(website, 'lxml')

print(soup.find(name="span", id="productTitle"))
