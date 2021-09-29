"""Добавление нового курса."""


import allure
import pytest
from models.create_course import CreateCourse as CD


@pytest.mark.create_course
class TestCourseCreation:
    @allure.testcase("TC-15")
    @allure.feature("create_course")
    @allure.story("Добавление основной информации о курсе")
    def test_general_data_course_creation(self, app, auth):
        """
        Steps.

            1. Open auth page
            2. Auth with valid data
            3. Check auth result
            4. Go to course creation page
            5. Add tag with valid data
            6. Check successfully editing.
        """
        app.login.go_to_editing_course_data()
        course_data = CD.random()
        app.create_course_general.edit_course_data(course_data)
        app.create_course_description.edit_description_course_data(course_data)
        app.create_course_images.edit_image_course(course_data.image_url)
        app.create_course_groups.edit_groups_info_course(course_data)
        app.create_course_tags.edit_tags_course(course_data)
        assert app.create_course_general.is_created(
            course_data.full_course_name
        ), "Course is not created!"
