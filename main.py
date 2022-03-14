import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

EMAIL = os.environ.get('EMAIL_LOGIN')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
MY_FUNDS = 36.00
AMAZON_URL = 'https://www.amazon.com/Magic-Gathering-Innistrad-Commander-Bloodline/dp/B099YJBTNF/'

header = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0',
    "Accept-Language": 'en-US'
}

response = requests.get(url=AMAZON_URL, headers=header)
website = response.text

soup = BeautifulSoup(website, 'lxml')

current_price = soup.find(name='span', class_='a-offscreen').getText()[1:]

if float(current_price) >= MY_FUNDS:
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=EMAIL, password=EMAIL_PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                        msg=f'Subject:MTG DECK ALERT\n\n Mtg commander deck is already in bargain price. Check it out!\nhttps://www.amazon.com/Magic-Gathering-Innistrad-Commander-Bloodline/dp/B099YJBTNF/')