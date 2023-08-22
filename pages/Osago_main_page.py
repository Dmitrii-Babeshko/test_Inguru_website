from base.base_class import Base
from utilities.logger import Logger
import allure


class Osago(Base):

    url = 'https://osago.finuslugi.ru/'

    #locators xpath
    gos_number_text = 'Р867СА47'
    cookies_xpath = '//*[@id="root"]/div/div[3]/div/button/i'
    gos_number_xpath = '//*[@id="__main__"]/div/div[1]/div/div[4]/form/div/input'
    calculate_button_xpath   = '//*[@id="__main__"]/div/div[1]/div/div[4]/form/button'

    #Getters
    def get_gos_number(self):
        return self.get_locator(self.gos_number_xpath)

    def get_calculate_button(self):
        return self.get_locator(self.calculate_button_xpath  )
    def get_cookies_button(self):
        return self.get_locator(self.cookies_xpath)

    #Actions
    def input_gos_number(self, text):
        self.get_gos_number().send_keys(text)
        print('Input gos number')
    def click_calculate_button(self):
        self.get_calculate_button().click()
        print('Click calculate button')

    def click_cookies_button(self):
        self.get_cookies_button().click()
        print('Click cookies button')

    #Methods

    def calculate_to_gos_number(self):
        with allure.step('calculate_to_gos_number'):
            Logger.add_start_step(method='calculate_to_gos_number')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_cookies_button()
            self.scroll_to_xpath_locator(self.gos_number_xpath)
            self.input_gos_number(self.gos_number_text)
            self.scroll_to_xpath_locator(self.calculate_button_xpath  )
            self.click_calculate_button()
            Logger.add_end_step(url=self.driver.current_url, method='calculate_to_gos_number')