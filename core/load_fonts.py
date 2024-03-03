"""
atomic function to load app fonts
"""

from .read_user_config import read_user_config


def load_fonts():
    font = read_user_config()["font"]
    font_size = read_user_config()["font_size"]

    fonts = {
        'Default': (font, font_size),
        'DefaultBold': (font, font_size, 'bold'),
        'Small': (font, int(round(float(font_size) * 0.75, 0))),
        'SmallBold': (font, int(round(float(font_size) * 0.75, 0)), 'bold'),
        'Large': (font, int(round(float(font_size) * 1.25, 0))),
        'LargeBold': (font, int(round(float(font_size) * 1.25, 0)), 'bold'),
        'ExtraLarge': (font, int(round(float(font_size) * 1.50, 0))),
        'ExtraLargeBold': (font, int(round(float(font_size) * 1.50, 0)), 'bold')
    }

    return fonts
