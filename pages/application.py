from pages.login_page import LoginPage
from pages.personal_data_page import PersonalDataPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.personal_data = PersonalDataPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")
