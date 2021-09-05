import random

from faker import Faker

from common.constants import PersonalDataConstants


fake = Faker("Ru-ru")


class PersonalData:
    def __init__(
        self,
        name=None,
        last_name=None,
        email=None,
        moodle_net_profile=None,
        email_display_mode=None,
        city=None,
        timezone=None,
        country_code=None,
        about=None,
        url=None,
        image_url=None,
        user_image_description=None,
    ):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.email_display_mode = email_display_mode
        self.moodle_net_profile = moodle_net_profile
        self.city = city
        self.timezone = timezone
        self.country_code = country_code
        self.about = about
        self.url = url
        self.image_url = image_url
        self.user_image_description = user_image_description

    @staticmethod
    def random():
        name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        email_display_mode = random.choice(
            list(PersonalDataConstants.EMAIL_DISPLAY_MODES.values())
        )
        moodle_net_profile = fake.url()
        city = fake.city_name()
        timezone = random.choice(PersonalDataConstants.TIMEZONE_VALUES)
        country_code = fake.country_code()
        about = fake.text(max_nb_chars=200)
        url = fake.url()
        image_url = fake.image_url()
        user_image_description = fake.text(max_nb_chars=20)
        return PersonalData(
            name,
            last_name,
            email,
            moodle_net_profile,
            email_display_mode,
            city,
            timezone,
            country_code,
            about,
            url,
            image_url,
            user_image_description,
        )
