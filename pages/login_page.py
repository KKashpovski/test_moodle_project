"""Интерактивное поведение страницы авторизации."""


import logging
from selenium.webdriver.remote.webelement import WebElement

from locators.admin_page_locators import CoursePageLocators
from models.auth import AuthData
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.personal_data_page_locators import PersonalDataPageLocators

logger = logging.getLogger("moodle")


class LoginPage(BasePage):
    def is_auth(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def confirm_exit_window(self):
        self.find_element(LoginPageLocators.FORM)
        element = self.find_elements(LoginPageLocators.CONFIRM_EXIT_BUTTON)
        if len(element) > 0:
            return True
        return False

    def email_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(LoginPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(LoginPageLocators.SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(LoginPageLocators.EXIT)

    def confirm_exit(self):
        return self.find_element(LoginPageLocators.CONFIRM_EXIT_BUTTON)

    def auth(self, data: AuthData):
        logger.info(f'User email is "{data.login}, user password {data.password}"')
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.confirm_exit_window():
            self.click_element(self.confirm_exit())
        self.fill_element(self.email_input(), data.login)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def user_menu_settings(self) -> WebElement:
        return self.find_element(LoginPageLocators.USER_MENU_SETTINGS)

    def go_to_editing_personal_data(self):
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(PersonalDataPageLocators.EDIT_INFO))

    def admin_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.ADMIN_BUTTON)

    def select_course_menu(self) -> WebElement:
        return self.find_element(LoginPageLocators.ADMIN_BUTTON)

    def go_to_editing_course_data(self):
        self.click_element(self.admin_menu())
        self.click_element(self.select_course_menu())
        self.click_element(self.find_element(CoursePageLocators.COURSE_TUB))
        self.click_element(self.find_element(CoursePageLocators.COURSE_CREATE_TUB))

    def auth_login_error(self) -> str:
        return self.find_element(LoginPageLocators.LOGIN_ERROR).text

    def sign_out(self):
        if self.is_auth():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.confirm_exit_window():
            self.click_element(self.confirm_exit())
