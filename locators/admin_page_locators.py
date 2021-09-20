"""Локаторы страницы администрирования."""


from selenium.webdriver.common.by import By


class CoursePageLocators:
    COURSE_TUB = (By.CSS_SELECTOR, "li:nth-of-type(3) > a[role='tab']")
    COURSE_CREATE_TUB = (By.CSS_SELECTOR, "div#linkcourses > .container > div:nth-of-type(1) > "
                                          ".col-sm-9 > .list-unstyled > li:nth-of-type(4) > a")

