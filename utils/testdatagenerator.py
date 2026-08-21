import random
import string

class TestDataGenerator:

    @staticmethod
    def random_username():
        return "user_" + ''.join(
            random.choices(string.ascii_letters + string.digits, k=8)
        )

    @staticmethod
    def random_password():
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        number = random.choice(string.digits)
        special = random.choice("@#$%")

        remaining = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6
            )
        )

        return uppercase + lowercase + number + special + remaining

    @staticmethod
    def random_employee_prefix():
        return random.choice(string.ascii_lowercase)