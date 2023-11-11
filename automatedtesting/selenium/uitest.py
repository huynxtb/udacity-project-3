from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime

LOGIN_URL = 'https://www.saucedemo.com/'

def timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{ts}\t"

def driver_config():
    print('Starting the browser...')
    options = ChromeOptions()
    return webdriver.Chrome(options=options)

def login(driver, user, password):
    driver.get(LOGIN_URL)
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    print(f"{timestamp()}Login successfully: user {user} password: {password}.")

def add_items_to_cart(driver, count):
    for i in range(count):
        element = f"a[id='item_{i}_title_link']"
        driver.find_element(By.CSS_SELECTOR, element).click()
        driver.find_element(By.CSS_SELECTOR, "button.btn_primary.btn_inventory").click()
        product = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text
        driver.find_element(By.CSS_SELECTOR, "button.inventory_details_back_button").click()
    print(f"{timestamp()}Added {count} items to cart.")

def remove_items_from_cart(driver):
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
    print(f"Begin remove {len(cart_items)} items in cart")
    for item in cart_items:
        item_name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
        item.find_element(By.CLASS_NAME, 'cart_button').click()
        print(f'Removed {item_name} from cart')
    print('Test Remove Items from cart Success.')

def run_test():
    driver = driver_config()
    print("Browser started!")
    print("Begin UI Test")
    login(driver, 'standard_user', 'secret_sauce')
    print("--Begin Add items to cart")
    add_items_to_cart(driver, 3)
    print("--End Add items to cart")
    print("--Begin Remove items from cart")
    remove_items_from_cart(driver)
    print("--End Remove items from cart")
    driver.quit()
    print("Completed")

if __name__ == "__main__":
    run_test()
