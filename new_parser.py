from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageEnhance
import os
import time

class Parser:
    def __init__(self, byfly_link, captcha_solve_link, profile, password):
        self.byfly_link = byfly_link
        self.captcha_solve_link = captcha_solve_link
        self.profile = profile
        self.password = password

    def byfly_registration(self):
        driver = webdriver.Chrome()
        driver.get(self.byfly_link)

        login_input = driver.find_element(By.ID, 'oper_user')
        login_input.send_keys(self.profile)

        password_input = driver.find_element(By.NAME, 'passwd')
        password_input.send_keys(self.password)

        save_captcha = driver.find_element(By.ID, 'capcher')
        save_captcha.screenshot('screenshots/first_captcha.png')

        captcha_text_input = driver.find_element(By.ID, 'cap_field')
        captcha_text_input.send_keys(self.get_text())

        enter = driver.find_element(By.CSS_SELECTOR, "input[value='Войти]")
        enter.click()

    def change_captcha(self):
        image = Image.open('screenshots/first_captcha.png')
        
        if image.mode != "RGB":
                image = image.convert("RGB")
        
        brightness_factor = 1.2
        enhancer_b = ImageEnhance.Brightness(image)
        bright_img = enhancer_b.enhance(brightness_factor)
    
        contrast_factor = 1.5
        enhancer_c = ImageEnhance.Contrast(bright_img)
        final_img = enhancer_c.enhance(contrast_factor)
    
        final_img = final_img.convert('1')
        final_img.save("screenshots/changed.png")
        os.remove('screenshots/first_captcha.png')

    def get_text(self):
        driver = webdriver.Chrome()
        driver.get(self.captcha_solve_link)
        img_input = driver.find_element(By.CSS_SELECTOR, "label[for='uploadFile']")
        img_input.send_keys(os.path.abspath('screenshots/changed.png'))
        os.remove('screenshots/changed.png')
        give_img = driver.find_element(By.CSS_SELECTOR, "div[style='pointer-events: auto;']")
        give_img.click()
        time.sleep(10)
        result_captcha = driver.find_element(By.ID, 'result__text0')
        return result_captcha
             

    def __del__(self):
        print('programm succesfuly finished')
