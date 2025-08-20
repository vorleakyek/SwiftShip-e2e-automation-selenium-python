from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_deal = (By.XPATH, "//p[contains(text(),'Deals for you')]/following-sibling::div//a")
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(), 'Add to Cart')]")
        self.continue_shopping_button = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
        self.checkout_button = (By.XPATH, "//button[contains(text(), 'Checkout')]")
        self.quantity_selection_button = (By.XPATH, "//select[@name='quantityOfItem']")

    def add_three_products_to_cart_with_changing_quantity(self):
        # collect all product links
        deal_links = self.driver.find_elements(*self.product_deal)
        # get first 2 only
        product_urls = [link.get_attribute("href") for link in deal_links[:3]]
        for i, url in enumerate(product_urls):
            try:
                self.driver.get(url)
                selection_options = Select(self.driver.find_element(*self.quantity_selection_button))
                selection_options.select_by_index(2)
                self.driver.find_element(*self.add_to_cart_button).click()
                if i != len(product_urls) - 1:
                    self.driver.find_element(*self.continue_shopping_button).click()
                else:
                    self.driver.find_element(*self.checkout_button).click()
            except Exception as e:
                self.driver.save_screenshot(f"step_{i}.png")
                raise

    def add_all_product_deals_for_you(self):
        # collect all product links
        deal_links = self.driver.find_elements(*self.product_deal)
        product_urls = [link.get_attribute("href") for link in deal_links]

        # loop each product url
        for i, url in enumerate(product_urls):
            try:
                # returns the full absolute URL, even if the HTML says /products/100
                self.driver.get(url)
                self.driver.find_element(*self.add_to_cart_button).click()

                if i != len(product_urls) - 1:
                    self.driver.find_element(*self.continue_shopping_button).click()
                else:
                    self.driver.find_element(*self.checkout_button).click()
            except Exception as e:
                self.driver.save_screenshot(f"step_{i}.png")
                print(f"x step {i} failed: {str(e)}")
                raise
