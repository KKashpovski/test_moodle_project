"""Application for app."""


from pages.login_page import LoginPage
from pages.personal_data_page import (
    PersonalDataPage,
    PersonalDataPageMore,
    PersonalDataPageOptional,
    PersonalDataPageTag,
)
from pages.create_course_page import (
    CreateCourseGeneral,
    CreateCourseDescription,
    CreateCourseImages,
    CreateCourseGroups,
    CreateCourseTags,
)


class Application:
    def __init__(self, driver, url):
        """Construct data."""
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.personal_data = PersonalDataPage(self)
        self.personal_data_more = PersonalDataPageMore(self)
        self.personal_data_optional = PersonalDataPageOptional(self)
        self.personal_data_tag = PersonalDataPageTag(self)
        self.create_course_general = CreateCourseGeneral(self)
        self.create_course_description = CreateCourseDescription(self)
        self.create_course_images = CreateCourseImages(self)
        self.create_course_groups = CreateCourseGroups(self)
        self.create_course_tags = CreateCourseTags(self)

    def open_main_page(self):
        """Open page."""
        self.driver.get(self.url)

    def quit(self):
        """Exit."""
        self.driver.quit()

    def open_auth_page(self):
        """Open login page."""
        self.driver.get(self.url + "/login/index.php")
