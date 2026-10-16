from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_capcha():
    driver = webdriver.Chrome()
    driver.get('https://www.prepostseo.com/ru/image-to-text')
    file_inp = os.path.abspath('result.png')
    # file_inp = os.path.abspath('captcha_temp/image.png')

    wait = WebDriverWait(driver, 10)
    captcah_code = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
    captcah_code.send_keys(file_inp)
    time.sleep(2)


    extrude_text_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div[4]/div[3]/div[1]')
    extrude_text_button.click()
    time.sleep(10)

    captcah_code = driver.find_element(By.XPATH, '//*[@id="result__text0"]').text
    return captcah_code