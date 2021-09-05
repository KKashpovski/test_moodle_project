"""Добавление личных данных."""


import pytest
import allure
from allure_commons.types import AttachmentType

from models.personal_data import PersonalData as PD


@pytest.mark.personal_data
class TestPersonalData:
    @allure.feature("authorisation")
    @allure.story("корректное обновление персональных данных")
    def test_valid_edit_basic_personal_data(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with valid data
        6. Check successfully editing
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data.edit_personal_data(personal_data)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Successful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert app.personal_data.is_changed(), "Personal data not changed!"

    @allure.feature("authorisation")
    @allure.story("обновление персональных данных без обязательных полей")
    @pytest.mark.parametrize("field", ["name", "last_name", "email"])
    def test_edit_basic_personal_data_without_required_field(self, app, auth, field):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with invalid data
        6. Check editing is not successfully
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, field, "")
        app.personal_data.edit_personal_data(personal_data)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Unsuccessful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @allure.feature("authorisation")
    @allure.story("обновление персональных данных с некорректным email")
    @pytest.mark.parametrize("email", ["kudimovaks.ru", "@yandex.ru", "111"])
    def test_edit_basic_personal_data_with_incorrect_email(self, app, auth, email):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit basic personal data with incorrect email
        6. Check editing is not successfully
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, "email", email)
        app.personal_data.edit_personal_data(personal_data)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Unsuccessful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (not app.personal_data.is_changed()), "Personal data should not be changed!"

    @allure.feature("authorisation")
    @allure.story("обновление персональных данных c некорректными именем и фамилией")
    @pytest.mark.parametrize("name, last_name", [
            ["123", "123"],
            ["---", "---"],
            ["\xbdR6\x10\x7f", "\xbdR6\x10\x7f"],
            [PD().random().url, PD().random().url],
            [PD().random().image_url, PD().random().image_url],
        ],
    )
    @pytest.mark.xfail
    @pytest.mark.bug
    def test_edit_incorrect_name_lastname(self, app, auth, name, last_name):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit name or(and) lastname as digits
        6. Check editing is not successfully
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, "name", name)
        setattr(personal_data, "last_name", last_name)
        app.personal_data.edit_personal_data(personal_data)
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Unsuccessful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @pytest.mark.set_user_image
    def test_set_user_image(self, app, auth):
        """
        Steps
        1. Open auth page
        2. Auth with valid data
        3. Check auth result
        4. Go to page with editing personal data
        5. Edit user image
        6. Check successfully editing
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data.set_user_image(
            r"D:\Ksenia\QA\Innopolis\Auto_QA_Python\Lesson_34-35\test_moodle_project"
            r"\tests\personal_data\test_image.png",
            personal_data.user_image_description,
        )
        allure.attach(
            app.personal_data.make_screenshot(),
            name="Successful_changing_screenshot",
            attachment_type=AttachmentType.PNG,
        )
        assert app.personal_data.is_user_image_changed(), "User image not changed!"
