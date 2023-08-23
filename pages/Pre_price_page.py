from base.base_class import Base
from utilities.logger import Logger
from time import sleep
import allure
from selenium.webdriver import Keys


class Pre_price(Base):

    #locators xpath
    model_xpath = '//*[@id="__main__"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/input'
    model_text = 'Qashqai'
    model_selector_xpath = '//*[@id="__main__"]/div/div[1]/div[2]/div[1]/div[2]/div/span[3]'
    another_model_in_selector_menu_xpath = '//*[@id="__main__"]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/ul/li[2]'
    clear_search_in_selector_menu_xpath = '//*[@id="__main__"]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/a'
    continue_button_xpath = '//button[@class="button button_theme_gray full-mobile-width"]'
    #Getters

    def get_model(self):
        return self.get_locator(self.model_xpath)
    def get_model_selector(self):
        return self.get_locator(self.model_selector_xpath)

    def get_another_model_in_selector_menu(self):
        return self.get_locator(self.another_model_in_selector_menu_xpath)

    def get_clear_search_in_selector_menu(self):
        return self.get_locator(self.clear_search_in_selector_menu_xpath)

    def get_continue_button(self):
        return self.get_locator(self.continue_button_xpath)

    #Actions
    def click_model_selector(self):
        self.get_model_selector().click()
        print('Click model selector')

    def click_another_model_in_selector_menu(self):
        self.get_another_model_in_selector_menu().click()
        print('Click another model in selector menu')

    def click_clear_search_in_selector_menu(self):
        self.get_clear_search_in_selector_menu().click()
        print('Click another model in selector menu')

    def input_model(self):
        self.get_model().send_keys(self.model_text)

    def click_continue_button(self):
        self.scroll_to_xpath_locator(self.continue_button_xpath)
        self.get_continue_button().click()
        print('Click continue button')

    #Methods

    def calculating(self):
        with allure.step('calculate_to_gos_number'):
            Logger.add_start_step(method='calculate_to_gos_number')
            self.click_model_selector()
            sleep(1)
            self.get_screenshot()
            self.click_another_model_in_selector_menu()
            sleep(1)
            self.get_screenshot()
            self.click_clear_search_in_selector_menu()
            sleep(1)
            self.get_screenshot()
            self.input_model()
            self.get_model().send_keys(Keys.ARROW_DOWN)
            self.get_model().send_keys(Keys.RETURN)
            self.click_continue_button()

            sleep(10)
            Logger.add_end_step(url=self.driver.current_url, method='calculate_to_gos_number')