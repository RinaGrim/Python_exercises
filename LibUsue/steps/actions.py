from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@when('загрузили страницу "{web}"')
def step_impl(context, web):
    if web == "Информационно-библиотечный комплекс УрГЭУ":
        context.driver.get("http://lib.usue.ru/")


@step('ввели в текстовое поле "{request}"')
def step_impl(context, request):
    if request.lower() == "запрос":
        search_text = context.driver.find_element(By.XPATH, "//*[@id='searchfield']")
        search_text.send_keys('dfjhkjlkmnbgfxcvgh')
    elif request.lower() == "python":
        key_words = context.driver.find_element_by_xpath("//*[@id='K_S21STR']")
        key_words.send_keys(f"{request}")
    elif request == "2012":
        start_year = context.driver.find_element_by_id('G_S21P06')
        start_year.send_keys(f"{request}")
    else:
        end_year = context.driver.find_element_by_id('G_S21P07')
        end_year.send_keys(f"{request}")


@step('нажали на "{element}" "{request}"')
def step_impl(context, element, request):
    if element == "кнопку":
        if request.lower().startswith("начать"):
            button_search = context.driver.find_element(By.XPATH, f"//*[@value='{request}']")
            button_search.click()
        elif request.lower().startswith("поиск"):
            btn_search = context.driver.find_element_by_xpath(f"//*[@value='{request}']")
            btn_search.click()
        else:
            alert = context.driver.switch_to.alert
            alert.accept()
    elif element == "пункт":
        if request.lower().startswith("электронный"):
            search_check = context.driver.find_element(By.XPATH, "//div[input[@value='999']]")
            search_check.click()
        elif request.lower().startswith("znanium"):
            search_check = context.driver.find_element(By.XPATH, "//div[input[@value='1']]")
            search_check.click()
        else:
            check_all_text = context.driver.find_element_by_name("CHECK21")
            check_all_text.click()
    elif element == "ссылку":
        find_elements = context.driver.find_element_by_xpath("//a[starts-with(text(), 'Всего:')]")
        context.driver.get(f"{find_elements.get_attribute('href')}")
    else:
        all_search = context.driver.find_element_by_xpath("//a[div[text()='Расширенный']]")
        str = f"{all_search.get_attribute('href')}"
        str = str.replace("'", "")
        str = str.partition("http")
        str1 = str[1] + str[2]
        context.driver.get(str1)


@when('загрузили всплывающее окно')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(EC.alert_is_present(), 'Выберите область для поиска')


@step('выбрали в списке "{name_list}" пункт "{item}"')
def step_impl(context, name_list, item):
    if name_list.lower().startswith("ключевые"):
        WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.XPATH, f"//*[text()='{item}']")))
        key_list = context.driver.find_element_by_xpath(f"//*[text()='{item}']")
        key_list.click()


@then("сделали скриншот окна результатов")
def step_impl(context):
    context.driver.save_screenshot("screens\\screenSite.jpg")
    time.sleep(4)