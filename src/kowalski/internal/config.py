from configparser import ConfigParser

from kowalski.internal.consts import CONFIG_PATH


def load_config():
    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config["DEFAULT"]["Path"], config["DEFAULT"]["Editor"]