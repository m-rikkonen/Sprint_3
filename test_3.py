
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ED

from config import url, email, password

def test_transfer_to_personal_account():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, 5).until(ED.visibility_of_element_located((By.XPATH, ".//a[@href='/account/profile']")))
    assert driver.find_element(By.XPATH, ".//a[@href='/account/profile']")
    driver.quit()

def test_transfer_from_personal_account_to_the_constructor_click_constructor():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//li/a[@href='/']")))
    driver.find_element(By.XPATH, ".//li/a[@href='/']").click()
    WebDriverWait(driver, 5).until(ED.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
    assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']")
    driver.quit()


def test_transfer_from_personal_account_to_the_constructor_click_logo():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")))
    driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']").click()
    WebDriverWait(driver, 5).until(ED.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))
    assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']")
    driver.quit()

def test_exit_from_account_by_button_exit():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input[@class='text input__textfield text_type_main-default']").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@class='text input__textfield text_type_main-default']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))
    driver.find_element(By.XPATH, ".//a[@href='/account']").click()
    WebDriverWait(driver, 5).until(ED.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    assert driver.find_element(By.CLASS_NAME, "Auth_login__3hAey")
    driver.quit()






