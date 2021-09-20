"""Модель страницы авторизации."""

from faker import Faker

fake = Faker("Ru-ru")


class AuthData:
    def __init__(self, login=None, password=None):
        """Construct data."""
        self.login = login
        self.password = password

    @staticmethod
    def random():
        """Random data."""
        login = fake.email()
        password = fake.password()
        return AuthData(login, password)
