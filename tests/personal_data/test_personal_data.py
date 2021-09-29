"""Добавление/обновление персональных данных."""


import os.path
import pytest
import allure
from models.personal_data import PersonalData as PD

current_dir = os.path.dirname(__file__)
user_images_directory = os.path.join(current_dir, "user_images")


@pytest.mark.personal_data
class TestPersonalData:
    @allure.testcase("TC-5")
    @allure.feature("add_or_edit_data")
    @allure.story("Добавление основных персональных данных")
    def test_valid_edit_basic_personal_data(self, app, auth):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Edit basic personal data with valid data
            6. Check successfully editing.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data.edit_personal_data(personal_data)
        assert app.personal_data.is_changed(), "Personal data not changed!"

    @allure.testcase("TC-6")
    @allure.testcase("TC-7")
    @allure.testcase("TC-8")
    @allure.feature("add_or_edit_data")
    @allure.story("Обновление персональных данных обязательных полей")
    @pytest.mark.parametrize("field", ["name", "last_name", "email"])
    def test_edit_basic_personal_data_without_required_field(self, app, auth, field):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Edit basic personal data with invalid data
            6. Check editing is not successfully.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, field, "")
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @allure.testcase("TC-9")
    @allure.feature("add_or_edit_data")
    @allure.story("Обновление персональных данных с некорректным email")
    @pytest.mark.parametrize("email", ["kudimovaks.ru", "@yandex.ru", "111"])
    def test_edit_basic_personal_data_with_incorrect_email(self, app, auth, email):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Edit basic personal data with incorrect email
            6. Check editing is not successfully.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, "email", email)
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @allure.testcase("TC-10")
    @allure.feature("add_or_edit_data")
    @allure.story("Обновление персональных данных c некорректными именем и фамилией.")
    @pytest.mark.parametrize(
        "name, last_name",
        [
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
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Edit name or(and) lastname as digits
            6. Check editing is not successfully.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        setattr(personal_data, "name", name)
        setattr(personal_data, "last_name", last_name)
        app.personal_data.edit_personal_data(personal_data)
        assert (
            not app.personal_data.is_changed()
        ), "Personal data should not be changed!"

    @allure.testcase("TC-11")
    @allure.feature("add_or_edit_data")
    @allure.story("Добавление изображения пользователя")
    @pytest.mark.set_user_image
    @pytest.mark.parametrize(
        "image_file",
        [
            os.path.join(user_images_directory, image)
            for image in os.listdir(user_images_directory)
        ],
    )
    def test_set_user_image(self, app, auth, image_file):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Edit user image
            6. Check successfully editing.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data.set_user_image(
            image_file, personal_data.user_image_description
        )
        assert app.personal_data.is_user_image_changed(), "User image not changed!"

    @allure.testcase("TC-12")
    @allure.feature("add_or_edit_data")
    @allure.story("Добавление персональных данных дополнительной информации об имени")
    def test_valid_edit_more_personal_data(self, app, auth):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Edit additional personal data with valid data
            6. Check successfully editing.
        """
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data_more.edit_personal_data_more(personal_data)
        assert app.personal_data_more.is_changed(), "Personal data not changed!"

    @allure.testcase("TC-13")
    @allure.feature("add_or_edit_data")
    @allure.story("Добавление персональных данных об интересах")
    def test_valid_edit_tag_personal_data(self, app, auth):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Add tag with valid data
            6. Check successfully editing.
        """
        app.open_main_page()
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data_tag.edit_personal_data_tag(personal_data)
        assert app.personal_data_tag.is_changed(), "Personal data not changed!"

    @allure.testcase("TC-14")
    @allure.feature("add_or_edit_data")
    @allure.story("Добавление персональных данных о необязательной информации")
    def test_valid_edit_optional_personal_data(self, app, auth):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to page with editing personal data
            5. Edit optional personal data with valid data
            6. Check successfully editing.
        """
        app.open_main_page()
        app.login.go_to_editing_personal_data()
        personal_data = PD.random()
        app.personal_data_optional.edit_personal_data_optional(personal_data)
        assert app.personal_data_optional.is_changed(), "Personal data not changed!"
