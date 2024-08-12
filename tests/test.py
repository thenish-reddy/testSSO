from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://sitetracker-ericssonglobal-eu01.my.salesforce.com/")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)
    sso_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id="idp_hint"]/button"))
    )
    sso_button.click()

    driver.quit()
