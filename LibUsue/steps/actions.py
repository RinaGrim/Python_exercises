from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyscreenshot as ImageGrab

# use_step_matcher("re")


@when('загрузится сайт "http://lib.usue.ru/" ввести "текст" в поле "поиск"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.driver = webdriver.Chrome()
        context.driver.get("http://lib.usue.ru/")
        search_text = context.driver.find_element_by_xpath("//*[@id='searchfield']")
        search_text.send_keys('dfjhkjlkmnbgfxcvgh')
    except:
        image = ImageGrab.grab()
        image.save("firstExcept.jpg")


@step('нажать на кнопку "Начать поиск!"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        button_search = context.driver.find_element_by_xpath("//*[@value='Начать поиск!']")
        button_search.click()
    except:
        ImageGrab.grab_to_file("secondExcept.jpg")


@when('появится всплывающее окно нажать кнопку "ОК"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        WebDriverWait(context.driver, 5).until(EC.alert_is_present(), 'Выберите область для поиска')
        alert = context.driver.switch_to.alert
        alert.accept()
    except:
        ImageGrab.grab_to_file("thirdExcept.jpg")


@then('отметить пункты "Электронный каталог ИБК УрГЭУ" и "Znanium.com"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        search_check = context.driver.find_elements_by_xpath("//div[@class='checkbox']")
        search_check[0].click()
        search_check[1].click()
    except:
        ImageGrab.grab_to_file("fourthExcept.jpg")


@when('загрузится страница {choice} нажать на {element} "{name_el}"')
def step_impl(context, choice, element, name_el):
    """
    :type context: behave.runner.Context
    """
    try:
        if choice == "результатов":
            find_elements = context.driver.find_element_by_xpath("//span[@class='totalfind']/a")
            context.driver.get(f"{find_elements.get_attribute('href')}")
        else:
            all_search = context.driver.find_element_by_xpath("//div[text()='Расширенный']/parent::a")
            str = f"{all_search.get_attribute('href')}"
            str = str.replace("'", "")
            str = str.partition("http")
            str1 = str[1] + str[2]
            context.driver.get(str1)
    except:
        ImageGrab.grab_to_file("fifthExcept.jpg")


@then('ввести в поисковое поле "{request}"')
def step_impl(context, request):
    """
    :type context: behave.runner.Context
    """
    try:
        if request == "Python":
            key_words = context.driver.find_element_by_xpath("//*[@id='K_S21STR']")
            key_words.send_keys('Python')
        elif request == "2012":
            start_year = context.driver.find_element_by_id('G_S21P06')
            start_year.send_keys('2012')
        else:
            end_year = context.driver.find_element_by_id('G_S21P07')
            end_year.send_keys('2018')
    except:
        ImageGrab.grab_to_file("sixthExcept.jpg")


@step('выбрать в списке пункт "PYTHON"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='PYTHON']")))
        key_list = context.driver.find_element_by_xpath("//*[text()='PYTHON']")
        key_list.click()
    except:
        ImageGrab.grab_to_file("seventhExcept.jpg")


@then('отметить пункт "Наличие полного текста"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        check_all_text = context.driver.find_element_by_name("CHECK21")
        check_all_text.click()
    except:
        ImageGrab.grab_to_file("eighthExcept.jpg")


@step('нажать на кнопку "Поиск"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        btn_search = context.driver.find_element_by_xpath("//*[@value='Поиск']")
        btn_search.click()
    except:
        ImageGrab.grab_to_file("ninethExcept.jpg")


@then("выйти из браузера")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.driver.save_screenshot("screenSite.jpg")
        time.sleep(5)
        context.driver.quit()
    except:
        ImageGrab.grab_to_file("tenthExcept.jpg")