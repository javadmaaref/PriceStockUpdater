import os
from web.selenium_manager import SeleniumManager

class WebUpdater:
    def __init__(self, username, password):
        self.selenium_manager = SeleniumManager()
        self.username = username
        self.password = password
        self.admin_login_url = os.getenv('ADMIN_LOGIN_URL')
        self.admin_update_url = os.getenv('ADMIN_UPDATE_URL')

    def update_products(self, products):
        self.selenium_manager.login(self.admin_login_url, self.username, self.password)
        for product in products:
            self._update_product(product)
        self.selenium_manager.quit()

    def _update_product(self, product):
        try:
            self.selenium_manager.navigate_to_product(self.admin_update_url, product['ID'])
            self.selenium_manager.update_product_name(product['Name'])
            self.selenium_manager.update_product_price(product['Final_Price'])
            self.selenium_manager.update_product_stock(product['Final_Stock'])
            self.selenium_manager.update_product_description(product['Description'])
            self.selenium_manager.save_product()
            print(f"Product {product['ID']} updated successfully.")
        except Exception as e:
            print(f"Error updating product {product['ID']}: {str(e)}")
