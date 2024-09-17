from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    button = browser.find_element(By.CLASS_NAME, 'card-body .btn')
    button.click()

    x_element = browser.find_element(By.CLASS_NAME, 'container .form-group .nowrap:nth-child(2)')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    submit = browser.find_element(By.CLASS_NAME, 'form-group .btn.btn-primary')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()