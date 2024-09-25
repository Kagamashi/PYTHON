# Selenium
# Selenium automates browsers, enabling tasks such as web scraping or testing.
from selenium import webdriver  # type: ignore
driver = webdriver.Chrome()
driver.get('https://www.example.com')
print(driver.title)
driver.quit()
