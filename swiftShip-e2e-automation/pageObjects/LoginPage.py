from selenium.webdriver.common.by import By

class LoginPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.user_email = "a@a.com"
        self.user_password = "123"
        self.sign_in_link = (By.LINK_TEXT, "Sign in")
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.sign_in_button = (By.XPATH, "//button[text()='Sign In']")

    def login(self):
        self.driver.get("http://ec2-54-177-188-240.us-west-1.compute.amazonaws.com/")
        self.driver.find_element(*self.sign_in_link).click()
        self.driver.find_element(*self.email_input).send_keys(self.user_email)
        self.driver.find_element(*self.password_input).send_keys(self.user_password)
        self.driver.find_element(*self.sign_in_button).click()
