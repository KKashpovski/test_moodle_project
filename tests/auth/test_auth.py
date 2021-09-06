"""Тестирование авторизации пользователя."""

import pytest
import allure
from allure_commons.types import AttachmentType
from common.constants import LoginConstants
from models.auth import AuthData


@pytest.mark.authorisation
class TestAuth:
    @allure.feature("authorisation")
    @allure.story("проверка на ввод существующего пользователя")
    def test_auth_valid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with valid data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData(login="kudimovaks@yandex.ru", password="Capita_123")
        app.login.auth(data)
        with allure.step("Делаем скриншот"):
            allure.attach(app.personal_data.make_screenshot(),
                          name="Screenshot_valid_data", attachment_type=AttachmentType.PNG)
        assert app.login.is_auth(), "We are not auth"

    @allure.feature("authorisation")
    @allure.story("проверка на ввод несуществующего пользователя")
    def test_auth_invalid_data(self, app):
        """
        Steps
        1. Open main page
        2. Auth with invalid data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        app.login.auth(data)
        with allure.step("Делаем скриншот"):
            allure.attach(app.personal_data.make_screenshot(),
                          name="Screenshot_invalid_data", attachment_type=AttachmentType.PNG)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"

    @allure.feature("authorisation")
    @allure.story("проверка на ввод пустых полей")
    @pytest.mark.parametrize("field", ["login", "password"])
    def test_auth_empty_data(self, app, field):
        """
        Steps
        1. Open main page
        2. Auth with empty data
        3. Check auth result
        """
        app.open_auth_page()
        data = AuthData.random()
        setattr(data, field, None)
        app.login.auth(data)
        with allure.step("Делаем скриншот"):
            allure.attach(app.personal_data.make_screenshot(),
                          name="Screenshot_none_data", attachment_type=AttachmentType.PNG)
        assert LoginConstants.AUTH_ERROR == app.login.auth_login_error(), "We are auth!"
