"""
atomic function to copy default_preferences.json into user_preferences.json
"""
import shutil

default_path = "resources/config/default_config.json"
user_path = "resources/config/user_config.json"


def reload_default_config():
    shutil.copy(default_path, user_path)
