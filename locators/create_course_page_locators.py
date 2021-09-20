"""Локаторы страницы создания курса."""


from selenium.webdriver.common.by import By


class CreateCourseGeneralLocators:
    FULL_NAME_COURSE = (By.CSS_SELECTOR, "input#id_fullname")
    NAME_COURSE = (By.CSS_SELECTOR, "input#id_shortname")
    COURSE_VISIBILITY = (By.CSS_SELECTOR, "select#id_visible")
    BEGIN_DAY_COURSE = (By.CSS_SELECTOR, "select#id_startdate_day")
    BEGIN_MONTH_COURSE = (By.CSS_SELECTOR, "select#id_startdate_month")
    BEGIN_YEAR_COURSE = (By.CSS_SELECTOR, "select#id_startdate_year")
    END_DAY_COURSE = (By.CSS_SELECTOR, "select#id_enddate_day")
    END_MONTH_COURSE = (By.CSS_SELECTOR, "select#id_enddate_month")
    END_YEAR_COURSE = (By.CSS_SELECTOR, "select#id_enddate_year")
    ID_COURSE = (By.CSS_SELECTOR, "input#id_idnumber")
    SAVE_BUTTON = (By.CSS_SELECTOR, "input#id_saveanddisplay")
    NAVBAR_ITEMS = (By.CLASS_NAME, "breadcrumb-item")
    COURSE_CREATE_HEADER = (By.TAG_NAME, "h1")


class CreateCourseDescriptionLocators:
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, ".editor_atto_content [dir]")


class CreateCourseImagesLocators:
    OPEN_IMAGE_MENU_BUTTON = (
        By.CSS_SELECTOR,
        "a[role='button'] > .fa.fa-file-o.fa-fw.icon",
    )
    DOWNLOAD_FILES_BY_URL = (
        By.CSS_SELECTOR,
        "div:nth-of-type(5) > .nav-link > .fp-repo-name",
    )
    FIELD_FOR_INPUT_URL = (By.CSS_SELECTOR, "input#fileurl")
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.fp-login-submit")
    IMAGE_BUTTON = (By.CSS_SELECTOR, ".fp-reficons2")
    SELECT_IMAGE_BUTTON = (By.CSS_SELECTOR, ".fp-select-confirm.btn")
    GO_TO_ALL_COURSES = (By.CSS_SELECTOR, "ol > li:nth-of-type(2) > a")
    COURSE_INFO_ICON = (
        By.CSS_SELECTOR,
        ".collapsed.coursebox.first.odd a[title='Описание'] > i[title='Описание']",
    )
    COURSE_INFO = (By.CSS_SELECTOR, ".coursebox.first.loaded.odd")
    COURSE_IMAGE = (By.CSS_SELECTOR, ".courseimage>img")


class CreateCourseGroupsLocators:
    GROUPS_DESCRIPTION = (By.CSS_SELECTOR, "#id_groups .ftoggler [role]")
    GROUP_MODE = (By.NAME, "groupmode")
    FORCED_GROUP_MODE = (By.XPATH, "/html//select[@id='id_groupmodeforce']")


class CreateCourseTagsLocators:
    TAGS_DESCRIPTION = (By.CSS_SELECTOR, "fieldset#id_tagshdr  a[role='button']")
    TAGS_FOR_COURSE = (
        By.XPATH,
        "/html//div[@id='fitem_id_tags']/div[2]//input[@role='combobox']",
    )
