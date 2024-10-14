import requests
from bs4 import BeautifulSoup
import time

class Scraper:
    def __init__(self, max_retries=3, base_retry_delay=5):
        self.max_retries = max_retries
        self.base_retry_delay = base_retry_delay

    def _get_soup(self, url):
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()
                return BeautifulSoup(response.content, 'html.parser')
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                retry_delay = self.base_retry_delay * (2 ** retries)
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retries += 1
        print("Max retries exceeded. Unable to fetch the page.")
        return None

class LionScraper(Scraper):
    def scrape(self, url):
        soup = self._get_soup(url)
        if not soup:
            return None, None

        product_counter_div = soup.find('div', class_='product-counter')
        stock = 1 if product_counter_div else 0

        price_div = soup.find('div', id='product-price')
        price = price_div.get('data-final-price') if price_div else None

        return price, stock

class TorobScraper(Scraper):
    def scrape(self, url):
        soup = self._get_soup(url)
        if not soup:
            return None

        buy_box = soup.find('div', class_='buy_box')
        if not buy_box:
            return None

        buy_box_text = buy_box.find_all('div', class_='buy_box_text')
        if len(buy_box_text) < 2 or 'تومان' not in buy_box_text[1].text:
            return None

        price_text = buy_box_text[1].text.split('تومان')[0].strip()
        return self._persian_to_english(price_text).replace('٫', '')

    @staticmethod
    def _persian_to_english(text):
        persian_digits = '۰۱۲۳۴۵۶۷۸۹'
        english_digits = '0123456789'
        translation_table = str.maketrans(persian_digits, english_digits)
        return text.translate(translation_table)
