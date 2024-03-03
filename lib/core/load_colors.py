"""
atomic function to load app theme colors
"""

from read_user_config import read_user_config


def load_colors():
    theme_color_1 = read_user_config()["theme_color_1"]
    theme_color_2 = read_user_config()["theme_color_2"]
    theme_color_3 = read_user_config()["theme_color_3"]
    # theme_color_4 = read_user_config()["theme_color_4"]

    colors = {
        'theme_color_1': theme_color_1,
        'theme_color_2': theme_color_2,
        'theme_color_3': theme_color_3
    }

    return colors
