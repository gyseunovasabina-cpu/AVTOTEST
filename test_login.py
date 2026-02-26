import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_login(browser):
    browser.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(browser, 10)

    # Ввод логина/пароля
    login_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    login_field.send_keys("tomsmith")
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Клик по кнопке
    login_button = browser.find_element(By.CLASS_NAME, "radius")
    login_button.click()

    # Проверка успеха
    success_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "subheader")))
    assert "Welcome" in success_element.text  # Меняй под реальный текст
