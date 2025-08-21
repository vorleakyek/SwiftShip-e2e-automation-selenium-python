from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Search:

    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.XPATH, "//form//input[@name='searchInput']")

    def search(self, search_term):
        search_input = self.driver.find_element(*self.search_input)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)






