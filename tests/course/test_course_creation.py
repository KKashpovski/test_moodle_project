"""Добавление нового курса."""


import pytest
from common.constants import AccountConstants
from models.auth import AuthData
from models.create_course import CreateCourse


@pytest.mark.create_course
class TestCourseCreation:
    def test_valid_course_creation(self, app):
        app.open_main_page()
        if not app.login.is_auth():
            app.open_auth_page()
            data = AuthData(login="kudimovaks@yandex.ru", password="Capita_123")
            app.login.auth(data)
            assert app.login.is_auth(), "You are not auth"
        app.login.go_to_administration_page()
        assert (
            AccountConstants.ADMINISTRATION == app.login.administration_page()
        ), "We are not on administration page! "
        app.login.go_to_course_page()
        app.login.go_to_create_course_page()
        assert (
            AccountConstants.CREATE_COURSE == app.create_course.create_course_page()
        ), "We are not on create course page!"
        course_info = CreateCourse.random()
        app.create_course.create_course(course_info)
        if app.create_course.is_created:
            assert course_info.full_course_name == app.create_course.new_course_page()
        else:
            return "The course was not created!"
