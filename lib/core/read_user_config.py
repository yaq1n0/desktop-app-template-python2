"""
atomic function to read user preferences from user_preferences.json
"""

from json import load

path = "resources/user_preferences.json"


def validate_all(_dict: dict) -> dict:
    numerics = ['font_size']
    booleans = ['enable_tooltips', 'enable_developer']
    hexadecimals = ['theme_color_1', 'theme_color_2', 'theme_color_3']

    # validate numerics
    for numeric in numerics:
        if type(_dict[numeric]) is not int:
            raise Exception("[read_user_config] one of the numerics failed to validate")

    # validate and postprocess booleans
    for boolean in booleans:
        if _dict[boolean] == "True":
            _dict[boolean] = True
        elif _dict[boolean] == "False":
            _dict[boolean] = False
        else:
            raise Exception("[read_user_config] one of the booleans failed to validate")

    # validate hexadecimals
    for hexadecimal in hexadecimals:
        valid_hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        if (_dict[hexadecimal][0] != "#") or (len(_dict[hexadecimal]) != 7):
            # doesn't start with # or  doesn't have 7 characters
            raise Exception("[read_user_config] one of the hexadecimals failed to validate")

        for char in (_dict[hexadecimal][1:]):
            if char not in valid_hex:
                raise Exception("[read_user_config] one of the hexadecimals failed to validate")

    return _dict


def read_user_config() -> dict:
    """ load the user_config file from path and performs validation and postprocessing """
    json_file = open(path, "r")
    json_dict = load(json_file)
    validated_dict = validate_all(json_dict)
    json_file.close()
    return validated_dict
