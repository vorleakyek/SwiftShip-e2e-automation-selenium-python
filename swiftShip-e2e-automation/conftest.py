import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

    if browser_name == "chrome":  # firefox
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(15)

    yield driver  # Run before the function execution
    time.sleep(5)
    driver.close()  # Run after the test function execution
