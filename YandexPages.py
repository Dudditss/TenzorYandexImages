from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class YandexSearchLocators:
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CLASS_NAME, "services-new__list-item")  # Локатор панели навигации
    LOCATOR_YANDEX_IMAGES = (By.CLASS_NAME, "PopularRequestList-Item")  # Локатор панели навигации
    LOCATOR_YANDEX_SEARCH_FIELD = (By.NAME, "text")  # Локатор поля поиска
    LOCATOR_YANDEX_IMAGES_RESULT = (By.CLASS_NAME, "serp-item")
    LOCATOR_YANDEX_MINI_IMAGES_RESULT = (By.CLASS_NAME, "MMGallery-Item_selected")
    LOCATOR_YANDEX_BUTTON_NEXT = (By.CLASS_NAME, "MediaViewer-ButtonNext")
    LOCATOR_YANDEX_BUTTON_PREV = (By.CLASS_NAME, "MediaViewer-ButtonPrev")

class ImagesHelper(BasePage):

    def search(self):  # Функция получения значения в поле ввода
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=10)
        return search_field.get_attribute('value')

    def check_navigation_bar(self):  # Функция получения элементов панели навигации
        all_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=5)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        all_list[3].click()
        time.sleep(1)
        return nav_bar_menu

    def images_bar(self):  # Функция перехода на 1-ую категорию картинок и возврат ее текстового значения
        images_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_IMAGES, time=5)
        images = [x.text for x in images_list if len(x.text) > 0]
        images_list[0].click()
        time.sleep(1)
        return images[0]

    def images_result(self):  # Функция перехода на 1-ую картинку
        images_result_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_RESULT, time=5)
        images_res = [x.text for x in images_result_list if len(x.text) > 0]
        images_result_list[0].click()
        time.sleep(1)
        return images_res

    def mini_images(self):
        mini_images_result_list = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_MINI_IMAGES_RESULT, time=5)
        return mini_images_result_list

    def button_next_click(self):
        button_next = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_BUTTON_NEXT, time=5)
        button_next.click()
        time.sleep(1)

    def button_prev_click(self):
        button_prev = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_BUTTON_PREV, time=5)
        button_prev.click()
        time.sleep(1)
