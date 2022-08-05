from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ED

from config import url


def test_go_to_the_buns_section():
    driver = webdriver.Chrome()
    driver.get(url)
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//h2[text()='Булки']")))
    assert driver.find_element(By.XPATH, ".//h2[text()='Булки']")
    driver.quit()

def test_go_to_the_sauces_section():
    driver = webdriver.Chrome()
    driver.get(url)
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))
    assert driver.find_element(By.XPATH, ".//h2[text()='Соусы']")
    driver.quit()

def test_go_to_the_fillings_section():
    driver = webdriver.Chrome()
    driver.get(url)
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    WebDriverWait(driver, 3).until(ED.visibility_of_element_located((By.XPATH, ".//h2[text()='Начинки']")))
    assert driver.find_element(By.XPATH, ".//h2[text()='Начинки']")
    driver.quit()




