
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ED

from config import url, email, password

def test_button_entry_log_in_to_account():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")
    driver.quit()

def test_button_entry_personal_account():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")
    driver.quit()

def test_button_entry_in_the_registration_form():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//a[@href='/register']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//a[@href='/login']")))
    driver.find_element(By.XPATH, ".//a[@href='/login']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH,".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")
    driver.quit()

def test_button_entry_in_the_password_recovery_form():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//a[@href='/forgot-password']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//a[@href='/login']")))
    driver.find_element(By.XPATH, ".//a[@href='/login']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']")
    driver.quit()

