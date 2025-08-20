

from selenium.webdriver.common.by import By

# from pageObjects.LoginPage import LoginPage
from pageObjects.ShopPage import ShopPage
# import webbrowser


def test_e2e(browser_instance):
    driver = browser_instance
    driver.get("http://ec2-54-177-188-240.us-west-1.compute.amazonaws.com/")

    # Test Case 1: Login and verify the email is displayed in the top right corner of the page
    # user_email = "a@a.com"
    # login_page = LoginPage(driver)
    # login_page.login()
    # email_text = driver.find_element(By.XPATH, "//p[contains(text(), '@')]").text
    # email = email_text.split("|")[0].strip()
    # assert user_email == email

    # Test Case 2: Add three items into the cart and go to the view cart page
    add_deal_items = ShopPage(driver)
    add_deal_items.add_three_products_to_cart_with_changing_quantity()

    # Test Case 3: Delete the first item and update the quantity of the last two items
    all_item_name_elements_in_cart = driver.find_elements(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div//h2")

    # step 1: delete the first item
    first_item_name = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[1]//h2"
    ).text
    first_item_delete_button = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[2]//div[1]/button"
    ).click()
    assert first_item_name not in all_item_name_elements_in_cart

    # Step 2:
    # all_item_name_elements_in_cart_after_deleting = driver.find_elements(
    #     By.XPATH,
    #     "//h1[contains(text(), 'My Cart')]/following-sibling::div//h2")

    # Verify that the order summary is correct
    # prices_elements = driver.find_elements(
    #     By.XPATH,
    #     "//h1[contains(text(), 'My Cart')]/following-sibling::div//span[contains(@class, 'text-rose-500')]"
    # )
    # prices = [float(price.text.split("$")[1]) for price in prices_elements]
    # expected_price = round(sum(prices), 2)
    # order_summary = driver.find_elements(By.XPATH, "//h3[contains(text(),'Order Summary')]/following-sibling::div//p")
    # display_price = round(float(order_summary[1].text.split("$")[1]), 2)
    # assert expected_price == display_price








    # webbrowser.open("report.html")

    # checkout




