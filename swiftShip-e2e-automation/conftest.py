import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="browser selection",
        choices=("chrome", "firefox", "safari"),
    )


@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    driver = None

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        # chrome_options.add_argument("--headless")            # 👈 Run in headless mode
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.implicitly_wait(5)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")           # 👈 Run in headless mode
        driver = webdriver.Firefox(service=service_obj, options=firefox_options)
        driver.implicitly_wait(15)

    yield driver  # before test
    time.sleep(5)
    driver.quit()  # after test
