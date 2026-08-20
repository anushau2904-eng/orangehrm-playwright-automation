import os
from configparser import ConfigParser
from pathlib import Path


class ConfigReader:

    _config = ConfigParser()

    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    CONFIG_FILE = PROJECT_ROOT / "config" / "config.ini"

    if CONFIG_FILE.exists():
        _config.read(CONFIG_FILE)

    @classmethod
    def get_URL(cls):
        if os.getenv("APP_URL"):
            return os.getenv("APP_URL")

        return cls._config.get("Application", "url")

    @classmethod
    def get_username(cls):
        if os.getenv("APP_USERNAME"):
            return os.getenv("APP_USERNAME")

        return cls._config.get("Credentials", "username")

    @classmethod
    def get_password(cls):
        if os.getenv("APP_PASSWORD"):
            return os.getenv("APP_PASSWORD")

        return cls._config.get("Credentials", "password")

    @classmethod
    def get_headless(cls):
        if os.getenv("HEADLESS"):
            return os.getenv("HEADLESS").lower() == "true"

        return cls._config.getboolean("Browser", "headless")

    @classmethod
    def get_slow_mo(cls):
        if os.getenv("SLOW_MO"):
            return int(os.getenv("SLOW_MO"))

        return cls._config.getint("Browser", "slow_mo")