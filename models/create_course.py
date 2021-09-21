"""Модель страницы создания курса."""


import random
from faker import Faker
from common.constants import CreateCourseConstants

fake = Faker("Ru-ru")


class CreateCourse:
    def __init__(
        self,
        full_course_name=None,
        course_name=None,
        course_visibility=None,
        begin_day=None,
        begin_month=None,
        begin_year=None,
        end_day=None,
        end_month=None,
        end_year=None,
        id_course=None,
        description_field=None,
        image_url=None,
        group_mode=None,
        forced_group_mode=None,
        tags_courses=None,
    ):
        """Construct data."""
        self.full_course_name = full_course_name
        self.course_name = course_name
        self.course_visibility = course_visibility
        self.begin_day = begin_day
        self.begin_month = begin_month
        self.begin_year = begin_year
        self.end_day = end_day
        self.end_month = end_month
        self.end_year = end_year
        self.id_course = id_course
        self.description_field = description_field
        self.image_url = image_url
        self.group_mode = group_mode
        self.forced_group_mode = forced_group_mode
        self.tags_courses = tags_courses

    @staticmethod
    def random():
        """Random data."""
        full_course_name = fake.bs()
        course_name = fake.company_suffix()
        course_visibility = str(random.randint(0, 1))
        begin_day = str(random.randint(1, 28))
        begin_month = str(random.randint(1, 12))
        begin_year = str(
            random.randint(
                CreateCourseConstants.CURRENT_BEGIN_YEAR,
                CreateCourseConstants.LAST_BEGIN_YEAR,
            )
        )
        end_day = str(random.randint(1, 28))
        end_month = str(random.randint(1, 12))
        end_year = str(
            random.randint(
                CreateCourseConstants.CURRENT_END_YEAR,
                CreateCourseConstants.LAST_END_YEAR,
            )
        )
        id_course = fake.iana_id()
        description_field = fake.text(max_nb_chars=200)
        image_url = (
            "https://sciencepop.ru/wp-content/uploads/"
            "2019/10/933c25cb1c62fb6c94a02260705faf02.jpg"
        )
        group_mode = str(random.randint(0, 2))
        forced_group_mode = str(random.randint(0, 1))
        tags_courses = fake.word()
        return CreateCourse(
            full_course_name,
            course_name,
            course_visibility,
            begin_day,
            begin_month,
            begin_year,
            end_day,
            end_month,
            end_year,
            id_course,
            description_field,
            image_url,
            group_mode,
            forced_group_mode,
            tags_courses,
        )
