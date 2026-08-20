from configparser import ConfigParser
# import os
from pathlib import Path

class ConfigReader:
    _config = ConfigParser()
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    _config.read(PROJECT_ROOT/"config"/"config.ini")

    @classmethod
    def get_URL(cls):
        return cls._config.get("Application", "url")
    @classmethod
    def get_username(cls):
        return cls._config.get("Credentials","username")
    @classmethod
    def get_password(cls):
        return cls._config.get("Credentials","password")

    @classmethod
    def get_headless(cls):
        return cls._config.getboolean("Browser" ,"headless")

    @classmethod
    def get_slow_mo(cls):
        return cls._config.getint("Browser" , "slow_mo")
    




# rootpath = os.path.dirname(os.path.dirname(__file__))
# config_path = os.path.join(rootpath, "config", "config.ini")



