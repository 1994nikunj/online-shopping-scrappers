import requests

import flipkart_item_restock_alert
from FlipkartScrapper.settings import url, headers

if __name__ == '__main__':
    r = requests.get(url, headers=headers)
    content = r.content
    flipkart_item_restock_alert.get_restock_alert(content)
