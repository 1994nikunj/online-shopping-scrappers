import datetime
import time
import winsound

from bs4 import BeautifulSoup


def get_restock_alert(content):
    soup = BeautifulSoup(content, features="html.parser")

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if soup.find(text='NOTIFY ME'):
            print('OUT OF STOCK| {}'.format(now))
        elif soup.find(text='BUY NOW') and soup.find(text='ADD TO CART'):
            winsound.Beep(frequency=700, duration=2000)
            print('ITEM FOUND| Time: {}'.format(now))
        time.sleep(5)
