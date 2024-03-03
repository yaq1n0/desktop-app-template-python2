""" AppState class """

# imports
from lib.functions import load_json_to_dict, write_json_from_dict


class PreferencesDict:
    """ PreferencesDict class, used to track preferences """

    def __init__(self):
        return

    def set_values_discrete(self, width, height, font, font_size, tooltips, dev):
        self.width, self.height, self.font, self.font_size, self.tooltips, self.dev = width, height, font, font_size, tooltips, dev

    def set_values_dict(self, preferences_dict):
        self.width = preferences_dict['width']
        self.height = preferences_dict['height']
        self.font = preferences_dict['font']
        self.font_size = preferences_dict['font_size']
        self.tooltips = preferences_dict['tooltips']
        self.dev = preferences_dict['dev']

    def validate_values(self):
        numerics = [self.width, self.height, self.font_size]
        booleans = [self.tooltips, self.dev]

        for numeric in numerics:
            if not numeric.isnumeric():
                raise Exception("[PreferencesDict.validate_numeric] Invalid numeric value] ")

        for boolean in booleans:
            if not isinstance(boolean, bool):
                raise Exception("[PreferencesDict.validate_boolean] Invalid boolean value")

    def asDict(self):
        return_dict = {
            "width": self.width
            , "height": self.height
            , "font": self.font
            , "font_size": self.font_size
            , "tooltips": self
            , "dev": self.dev
        }

        return return_dict


class AppState:
    """ AppState class """
    """ a singleton instance of appState class will be used to represent the global state of the app """

    def __init__(self):
        self.user_preferences = PreferencesDict()
        self.fonts = None

        self.reload()

    def reload(self):
        self.load_user_preferences()
        self.generate_fonts()

    def load_user_preferences(self):
        self.user_preferences.set_values_dict(load_json_to_dict("resources/user_preferences.json"))
        self.user_preferences.validate_values()

    def write_user_preferences(self):
        self.user_preferences.validate_values()
        write_json_from_dict("resources/user_preferences.json", self.user_preferences.asDict())

    def reset_defaults(self):
        defaults = load_json_to_dict("resources/default_user_preferences.json")
        self.user_preferences.set_values_dict(defaults)
        write_json_from_dict("resources/user_preferences.json", defaults)

    def generate_fonts(self):
        font = self.user_preferences.asDict()["font"]
        font_size = self.user_preferences.asDict()["font_size"]

        _generated_fonts = {
            'Default': (font, font_size),
            'DefaultBold': (font, font_size, 'bold'),
            'Small': (font, int(round(float(font_size) * 0.75, 0))),
            'SmallBold': (font, int(round(float(font_size) * 0.75, 0)), 'bold'),
            'Large': (font, int(round(float(font_size) * 1.25, 0))),
            'LargeBold': (font, int(round(float(font_size) * 1.25, 0)), 'bold'),
            'ExtraLarge': (font, int(round(float(font_size) * 1.50, 0))),
            'ExtraLargeBold': (font, int(round(float(font_size) * 1.50, 0)), 'bold')
        }

        return _generated_fonts
