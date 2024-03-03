"""
atomic function to copy default_preferences.json into user_preferences.json
"""
import shutil

default_path = "resources/default_preferences.json"
user_path = "resources/user_preferences.json"


def reload_default_config():
    shutil.copy(default_path, user_path)
