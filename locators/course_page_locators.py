from selenium.webdriver.common.by import By


class CoursePageLocators:
    COURSES_HEADER = (By.XPATH, "//a[@href='#linkcourses']")
    CREATE_COURSE_LINK = (
        By.XPATH,
        "//a[@href='https://qacoursemoodle.innopolis.university/course/edit.php"
        "?category=0']",
    )
