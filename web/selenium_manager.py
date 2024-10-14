from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumManager:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def login(self, login_url, username, password):
        self.driver.get(login_url)

        # Update these selectors to match your admin panel
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(EC.url_changes(login_url))

    def navigate_to_product(self, update_url, product_id):
        self.driver.get(f"{update_url}?id={product_id}")

    def update_product_name(self, name):
        name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )
        name_input.clear()
        name_input.send_keys(name)

    def update_product_price(self, price):
        price_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'price'))
        )
        price_input.clear()
        price_input.send_keys(str(price))

    def update_product_stock(self, stock):
        stock_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'mojudi'))
        )
        stock_input.clear()
        stock_input.send_keys(str(stock))

    def update_product_description(self, description):
        div_editor = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "cke_1_contents"))
        )
        iframe = div_editor.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(iframe)
        
        description_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        description_input.clear()
        if description and description.strip():
            description_input.send_keys(description)
        
        self.driver.switch_to.default_content()

    def save_product(self):
        save_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'submit'))
        )
        save_button.click()

    def quit(self):
        self.driver.quit()
