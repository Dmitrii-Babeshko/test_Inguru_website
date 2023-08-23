from time import sleep
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.Osago_main_page import Osago
from base.base_class import experimental_option_browser_stay_opened, load_strategy, path_of_chromedriver
from pages.Pre_price_page import Pre_price

@allure.description('Test osago bug №1')
def test_osago_bug_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", experimental_option_browser_stay_opened)  # False/True Закрытие/нет браузера
    options.page_load_strategy = load_strategy  # normal/eager/none загружать/нет полностью страницы
    service = Service(path_of_chromedriver)
    driver = webdriver.Chrome(service=service, options=options)

    print('Start test 1')

    osago = Osago(driver)
    osago.calculate_to_gos_number()
    pre_price = Pre_price(driver)
    pre_price.calculating()

