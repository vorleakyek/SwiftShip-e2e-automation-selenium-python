from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.ShopPage import ShopPage


def test_e2e(browser_instance):
    driver = browser_instance
    driver.get("http://ec2-54-177-188-240.us-west-1.compute.amazonaws.com/")

    # Test Case 1: Login and verify the email is displayed in the top right corner of the page
    user_email = "a@a.com"
    login_page = LoginPage(driver)
    login_page.login()
    email_text = driver.find_element(By.XPATH, "//p[contains(text(), '@')]").text
    email = email_text.split("|")[0].strip()
    assert user_email == email

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

    # Step 2: change the quantity of the first item to 1 less
    first_item_quantity_original = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[2]//div[2]/div"
    ).text
    subtract_btn_element = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[2]//div[2]/button[1]"
    )
    subtract_btn_element.click()
    first_item_quantity_updated = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[2]//div[2]/div"
    ).text
    assert int(first_item_quantity_original) - 1 == int(first_item_quantity_updated)

    # Step 3: change the quantity of the second item to 1 more
    second_item_quantity_original = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[4]//div[2]/div"
    ).text
    addition_btn_element = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[4]//div[2]/button[2]"
    )
    addition_btn_element.click()
    second_item_quantity_updated = driver.find_element(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div[4]//div[2]/div"
    ).text
    assert int(second_item_quantity_original) + 1 == int(second_item_quantity_updated)

    # Step 4: verify that the order summary is correct
    prices_elements = driver.find_elements(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div//span[contains(@class, 'text-rose-500')]"
    )
    quantity_elements = driver.find_elements(
        By.XPATH,
        "//h1[contains(text(), 'My Cart')]/following-sibling::div//div[contains(@class, 'px-2')]"
    )
    prices = [float(price.text.split("$")[1]) for price in prices_elements]
    quantities = [int(quantity.text) for quantity in quantity_elements]
    expected_prices = [price * quantity for price, quantity in zip(prices, quantities)]
    expected_price_all_items = round(sum(expected_prices), 2)
    expected_total_items = sum(quantities)
    expected_tax = round(expected_price_all_items * 0.1,2)
    expected_shipping = 8.99 if expected_price_all_items < 35 else 0
    expected_total_price = round(expected_price_all_items + expected_tax + expected_shipping,2)

    order_summary = driver.find_elements(By.XPATH, "//h3[contains(text(),'Order Summary')]/following-sibling::div//p")
    display_total_items = int(order_summary[0].text.split(":")[1].strip())
    display_price_all_items = round(float(order_summary[1].text.split("$")[1]), 2)
    display_tax = round(float(order_summary[2].text.split("$")[1]), 2)
    display_shipping = order_summary[3].text.split(":")[1].strip()
    display_total_price = round(float(order_summary[4].text.split("$")[1]), 2)

    assert expected_total_items == display_total_items
    assert expected_price_all_items == display_price_all_items
    assert display_shipping == "Free"
    assert expected_tax == display_tax
    assert expected_total_price == display_total_price






