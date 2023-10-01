from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element(by=By.ID, value="money")

cookie_button = driver.find_element(by=By.ID, value="cookie")

store = driver.find_elements(by=By.CSS_SELECTOR,value="#store div")
store_items = [item.get_attribute("id") for item in store]
print(store_items)

cpers = driver.find_element(by=By.ID, value="cps")

faive_min = time.time() + 5*60
after_5_sec =time.time() + 5


while True:
    cookie_button.click()
    if time.time() > after_5_sec:


        all_prices = driver.find_elements(by=By.CSS_SELECTOR,value="#store div b")
        item_prices = []

        for price in all_prices:
            e_text = price.text
            if e_text != "":
                cost = int(e_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = store_items[n]
            print(cookie_upgrades)

        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

     # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        after_5_sec= time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > faive_min:
            cookie_per_s = driver.find_element_by_id("cps").text
            print(cookie_per_s)
            break





