"""Страница создания курса."""


import logging
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.create_course_page_locators import CreateCourseGeneralLocators, \
    CreateCourseDescriptionLocators, CreateCourseImagesLocators, \
    CreateCourseGroupsLocators, CreateCourseTagsLocators


logger = logging.getLogger("moodle")


class CreateCourseGeneral(BasePage):
    def full_name_course(self) -> WebElement:
        return self.find_clickable_element(CreateCourseGeneralLocators.FULL_NAME_COURSE)

    def input_full_name_course(self, full_course_name) -> WebElement:
        return self.fill_element(self.full_name_course(), full_course_name)

    def name_course(self) -> WebElement:
        return self.find_clickable_element(CreateCourseGeneralLocators.NAME_COURSE)

    def input_name_course(self, course_name) -> WebElement:
        return self.fill_element(self.name_course(), course_name)

    def course_visibility(self) -> WebElement:
        course_visibility = self.find_select_element(
            CreateCourseGeneralLocators.COURSE_VISIBILITY
        )
        return course_visibility

    def select_course_visibility(self, value):
        return self.select_value(self.course_visibility(), value)

    def begin_day_course(self) -> WebElement:
        begin_day_course = self.find_select_element(
            CreateCourseGeneralLocators.BEGIN_DAY_COURSE
        )
        return begin_day_course

    def begin_month_course(self) -> WebElement:
        begin_month_course = self.find_select_element(
            CreateCourseGeneralLocators.BEGIN_MONTH_COURSE
        )
        return begin_month_course

    def begin_year_course(self) -> WebElement:
        begin_year_course = self.find_select_element(
            CreateCourseGeneralLocators.BEGIN_YEAR_COURSE
        )
        return begin_year_course

    def end_day_course(self) -> WebElement:
        end_day_course = self.find_select_element(
            CreateCourseGeneralLocators.END_DAY_COURSE
        )
        return end_day_course

    def end_month_course(self) -> WebElement:
        end_month_course = self.find_select_element(
            CreateCourseGeneralLocators.END_MONTH_COURSE
        )
        return end_month_course

    def end_year_course(self) -> WebElement:
        end_year_course = self.find_select_element(
            CreateCourseGeneralLocators.END_YEAR_COURSE
        )
        return end_year_course

    def id_course(self) -> WebElement:
        return self.find_element(CreateCourseGeneralLocators.ID_COURSE)

    def save_button(self) -> WebElement:
        return self.find_element(CreateCourseGeneralLocators.SAVE_BUTTON)

    def select_begin_day_course(self, value):
        return self.select_value(self.begin_day_course(), value)

    def select_begin_month_course(self, value):
        self.select_value(self.begin_month_course(), value)

    def select_begin_year_course(self, value):
        self.select_value(self.begin_year_course(), value)

    def select_end_day_course(self, value):
        self.select_value(self.end_day_course(), value)

    def select_end_month_course(self, value):
        self.select_value(self.end_month_course(), value)

    def select_end_year_course(self, value):
        self.select_value(self.end_year_course(), value)

    def input_id_course(self, id) -> WebElement:
        return self.fill_element(self.id_course(), id)

    def submit_button(self) -> WebElement:
        return self.find_element(CreateCourseGeneralLocators.SAVE_BUTTON)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_course_data(self, data):
        logger.info(
            f"Editing course data with next values:\n"
            f"full_course_name: {data.full_course_name}\n"
            f"course_name: {data.course_name}\n"
            f"course_visibility: {data.course_visibility}\n"
            f"begin_day: {data.begin_day}\n"
            f"begin_month: {data.begin_month}\n"
            f"begin_year: {data.begin_year}\n"
            f"end_day: {data.end_day}\n"
            f"end_month: {data.end_month}\n"
            f"end_year: {data.end_year}\n"
            f"id_course: {data.id_course}\n"
        )
        self.input_full_name_course(data.full_course_name)
        self.input_name_course(data.course_name)
        self.select_course_visibility(data.course_visibility)
        self.select_begin_day_course(data.begin_day)
        self.select_begin_month_course(data.begin_month)
        self.select_begin_year_course(data.begin_year)
        self.select_end_day_course(data.end_day)
        self.select_end_month_course(data.end_month)
        self.select_end_year_course(data.end_year)
        self.input_id_course(data.id_course)

    def is_changed(self, wait_time=10):
        header_user_info_elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(
                CreateCourseGeneralLocators.NAVBAR_ITEMS
            ),
            message=f"Can't find elements by locator "
            f"{CreateCourseGeneralLocators.NAVBAR_ITEMS}",
        )
        if len(header_user_info_elements) == 4:
            return True
        else:
            return False

    def is_created(self, course_name, wait_time=10):
        header = self.find_element(CreateCourseGeneralLocators.COURSE_CREATE_HEADER)
        header_text = self.get_element_text(header)
        return header_text == course_name


class CreateCourseDescription(CreateCourseGeneral):
    def description_field(self) -> WebElement:
        return self.find_element(CreateCourseDescriptionLocators.DESCRIPTION_FIELD)

    def input_description_course(self, text) -> WebElement:
        return self.fill_element(self.description_field(), text)

    def submit_button(self) -> WebElement:
        return self.find_element(CreateCourseGeneralLocators.SAVE_BUTTON)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_description_course_data(self, data):
        logger.info(f"input_description_course: {data.description_field}\n")
        self.input_description_course(data.description_field)


class CreateCourseImages(CreateCourseGeneral):
    def open_image_menu_button(self) -> WebElement:
        return self.find_clickable_element(
            CreateCourseImagesLocators.OPEN_IMAGE_MENU_BUTTON
        )

    def download_files_input_url(self) -> WebElement:
        return self.find_clickable_element(
            CreateCourseImagesLocators.DOWNLOAD_FILES_BY_URL
        )

    def field_for_input_url(self) -> WebElement:
        return self.find_clickable_element(
            CreateCourseImagesLocators.FIELD_FOR_INPUT_URL
        )

    def download_button(self) -> WebElement:
        return self.find_clickable_element(CreateCourseImagesLocators.DOWNLOAD_BUTTON)

    def image_button(self) -> WebElement:
        return self.find_clickable_element(CreateCourseImagesLocators.IMAGE_BUTTON)

    def select_image_button(self) -> WebElement:
        return self.find_clickable_element(
            CreateCourseImagesLocators.SELECT_IMAGE_BUTTON
        )

    def edit_image_course(self, image_url):
        logger.info(f"url for download image: {image_url}\n")
        self.click_element(self.open_image_menu_button())
        self.click_element(self.download_files_input_url())
        self.click_element(self.field_for_input_url())
        self.fill_element(self.field_for_input_url(), image_url)
        self.click_element(self.download_button())
        self.click_element(self.image_button())
        self.click_element(self.select_image_button())
        time.sleep(3)


class CreateCourseGroups(CreateCourseGeneral):
    def groups_description(self) -> WebElement:
        return self.find_clickable_element(
            CreateCourseGroupsLocators.GROUPS_DESCRIPTION
        )

    def open_groups_description(self):
        self.click_element(self.groups_description())

    def group_mode(self) -> WebElement:
        return self.find_select_element(CreateCourseGroupsLocators.GROUP_MODE)

    def select_group_mode(self, value):
        return self.select_value(self.group_mode(), value)

    def forced_group_mode(self) -> WebElement:
        return self.find_select_element(CreateCourseGroupsLocators.FORCED_GROUP_MODE)

    def select_forced_group_mode(self, value):
        return self.select_value(self.forced_group_mode(), value)

    def edit_groups_info_course(self, data):
        logger.info(
            f"select_group_mode: {data.group_mode}\n"
            f"select_forced_group_mode: {data.forced_group_mode}\n"
        )
        time.sleep(3)
        self.open_groups_description()
        time.sleep(5)
        self.select_group_mode(data.group_mode)
        time.sleep(5)
        self.select_forced_group_mode(data.forced_group_mode)


class CreateCourseTags(CreateCourseGeneral):
    def tags_description(self) -> WebElement:
        return self.find_clickable_element(CreateCourseTagsLocators.TAGS_DESCRIPTION)

    def open_tags_description(self):
        self.click_element(self.tags_description())

    def tags_for_course(self) -> WebElement:
        return self.find_clickable_element(CreateCourseTagsLocators.TAGS_FOR_COURSE)

    def input_tags_for_course(self, word) -> WebElement:
        return self.fill_element(self.tags_for_course(), word)

    def edit_tags_course(self, data):
        logger.info(f"input_tags_for_course: {data.tags_courses}\n")
        self.open_tags_description()
        self.input_tags_for_course(data.tags_courses)
        self.submit_changes()
