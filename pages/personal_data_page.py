from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from pages.base_page import BasePage
from locators.personal_data_page_locators import PersonalDataPageLocators


class PersonalDataPage(BasePage):
    def basic_data(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.BASIC_DATA)

    def name_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.NAME_INPUT)

    def lastname_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.LASTNAME_INPUT)

    def email_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.EMAIL_INPUT)

    def email_display_select(self) -> WebElement:
        email_display = self.find_select_element(PersonalDataPageLocators.EMAIL_DISPLAY)
        return email_display

    def moodle_net_profile_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.MOODLE_NET_PROFILE)

    def city_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.CITY_INPUT)

    def country_select(self) -> WebElement:
        country_select = self.find_select_element(
            PersonalDataPageLocators.COUNTRY_SELECT
        )
        return country_select

    def timezone_select(self) -> WebElement:
        country_select = self.find_select_element(
            PersonalDataPageLocators.TIMEZONE_SELECT
        )
        return country_select

    def about_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.ABOUT)

    def user_image_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.USER_IMAGE_INPUT)

    def input_user_image(self, image_file):
        self.fill_element(self.user_image_input(), image_file)

    def user_image_file_add_button(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.USER_IMAGE_FILE_ADD_BUTTON
        )

    def user_image_file_choose_input(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.USER_IMAGE_FILE_CHOOSE_INPUT
        )

    def download_file_button(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.DOWNLOAD_FILE_BUTTON
        )

    def user_image_description_input(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.USER_IMAGE_DESCRIPTION
        )

    def submit_button(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.SUBMIT_BUTTON)

    def input_name(self, name):
        self.fill_element(self.name_input(), name)

    def input_lastname(self, lastname):
        self.fill_element(self.lastname_input(), lastname)

    def input_email(self, email):
        self.fill_element(self.email_input(), email)

    def select_email_display(self, value):
        self.select_value(self.email_display_select(), value)

    def input_moodle_net_profile(self, url):
        self.fill_element(self.moodle_net_profile_input(), url)

    def input_city(self, city):
        self.fill_element(self.city_input(), city)

    def select_country(self, value):
        self.select_value(self.country_select(), value)

    def select_timezone(self, value):
        self.select_value(self.timezone_select(), value)

    def input_about(self, text):
        self.fill_element(self.about_input(), text)

    def choose_user_image_file(self, image_file):
        self.click_element(self.user_image_file_add_button())
        self.fill_element(self.user_image_file_choose_input(), image_file)
        self.click_element(self.download_file_button())

    def input_user_image_description(self, text):
        self.fill_element(self.user_image_description_input(), text)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_personal_data(self, data):
        self.input_name(data.name)
        self.input_lastname(data.last_name)
        self.input_email(data.email)
        self.select_email_display(data.email_display_mode)
        self.input_moodle_net_profile(data.moodle_net_profile)
        self.input_city(data.city)
        self.select_country(data.country_code)
        self.select_timezone(data.timezone)
        self.input_about(data.about)
        self.submit_changes()

    def set_user_image(self, image_file, user_image_description):
        sleep(5)
        self.execute_js("document.querySelector('input#id_imagefile').type='';")
        sleep(5)
        self.input_user_image(image_file)
        sleep(5)
        self.input_user_image_description(user_image_description)
        sleep(5)
        self.submit_changes()
        sleep(5)
        # self.choose_user_image_file(image_file)
        # self.input_user_image_description(user_image_description)
        # self.submit_changes()

    def is_changed(self, wait_time=10):
        header_user_info_elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(PersonalDataPageLocators.NAVBAR_ITEMS),
            message=f"Can't find elements by locator "
            f"{PersonalDataPageLocators.NAVBAR_ITEMS}",
        )
        if len(header_user_info_elements) == 2:
            return True
        else:
            return False

    def is_user_image_changed(self):
        if self.is_changed() and not self.find_elements(
                PersonalDataPageLocators.USER_PROFILE_DEFAULT_PICTURE
        ):
            return True
        else:
            return False
