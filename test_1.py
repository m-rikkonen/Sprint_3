
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ED

from config import url, name, email, password, bad_pass


def test_registration_true():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//a[@href='/register']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//button[text()='Зарегистрироваться']")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(name)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[3]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    assert driver.find_element(By.CLASS_NAME, "Auth_login__3hAey")
    driver.quit()

def test_registration_error():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//a[@href='/register']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//button[text()='Зарегистрироваться']")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(name)
    driver.find_element(By.XPATH,".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH,".//fieldset[3]//input[@class='text input__textfield text_type_main-default']").send_keys(bad_pass)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))
    assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']")

    driver.quit()
