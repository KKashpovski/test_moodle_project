"""Задание констант."""


class LoginConstants:
    AUTH_ERROR = "Неверный логин или пароль, попробуйте заново."


class PersonalDataConstants:
    EMAIL_DISPLAY_MODES = {
        "hidden": "0",
        "all_can_see": "1",
        "show_to_course_participants": "2",
    }
    TIMEZONE_VALUES = (
        "99",  # server's timezone
        "Asia/Dubai",
        "America/Santiago",
        "Africa/Tunis",
        "Europe/Moscow",
        "Europe/Moscow",
        "UTC",
    )


class CreateCourseConstants:
    CURRENT_BEGIN_YEAR = 2021
    LAST_BEGIN_YEAR = 2023
    CURRENT_END_YEAR = 2024
    LAST_END_YEAR = 2050

