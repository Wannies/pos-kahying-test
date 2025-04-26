from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def test_shipping_malaysia_to_india():
    driver = webdriver.Chrome()
    driver.get("https://pos.com.my/send/ratecalculator")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # From Postcode: 35600
    from_postcode = driver.find_element(By.CSS_SELECTOR, "div[class='d-flex mt-4'] div[class='mr-03'] input[placeholder='Postcode'")
    from_postcode.clear()
    from_postcode.send_keys("35600")
    time.sleep(1)

    # To Country: India
    to_country = driver.find_element(By.XPATH, "//input[@id='mat-input-0']")
    to_country.clear()
    to_country.send_keys("India")
    time.sleep(1)
    dropdown_country = driver.find_element(By.XPATH, "//div[@id='mat-autocomplete-0']")
    dropdown_country.click()
    time.sleep(1)

    # Weight: 1
    weight_field = driver.find_element(By.XPATH, "//input[@placeholder='eg. 0.1kg']")
    weight_field.clear()
    weight_field.send_keys("1")

    # Click Calculate
    calculate_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Calculate')]")
    calculate_btn.click()

    # Wait for results and assert at least one quote is shown
    results_section = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".bg-white.ng-star-inserted")))
    assert len(results_section) > 0, "No shipping options were displayed."

    # Verify that there is more than one quote
    quote_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Book Now')]")))
    assert len(quote_cards) > 1, f"Expected multiple quotes, but found {len(quote_cards)}."
    print(f"✅ {len(quote_cards)} shipping quotes found.")

    driver.quit()

if __name__ == "__main__":
    test_shipping_malaysia_to_india()
