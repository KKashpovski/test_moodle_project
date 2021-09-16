"""Локаторы страницы авторизации."""


from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "loginbtn")
    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
    USER_MENU_SETTINGS = (By.ID, "actionmenuaction-5")
    CONFIRM_EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "#signup > button")
    PAGE_MENU_BUTTON = (By.CLASS_NAME, "btn nav-link float-sm-left mr-1 btn-light bg-gray")
    ADMIN_BUTTON = (By.CSS_SELECTOR,
                    "div#nav-drawer > nav:nth-of-type(2) > ul > li > a > div > div > span:nth-of-type(2)")
