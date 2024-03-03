"""
atomic function to write to user_preferences.json
"""

from json import dump

path = "lib/resources/user_config.json"


def validate_all(_dict: dict) -> dict:
    numerics = ['font_size']
    booleans = ['enable_tooltips', 'enable_developer']
    hexadecimals = ['theme_color_1', 'theme_color_2', 'theme_color_3']

    # validate numerics
    for numeric in numerics:
        if type(_dict[numeric]) is not int:
            raise Exception("[write_user_config] one of the numerics failed to validate")

    # validate and postprocess booleans
    for boolean in booleans:
        if _dict[boolean] == True:
            _dict[boolean] = "True"
        elif _dict[boolean] == False:
            _dict[boolean] = "False"
        else:
            raise Exception("[write_user_config] one of the booleans failed to validate")

    # validate hexadecimals
    for hexadecimal in hexadecimals:
        valid_hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        if (_dict[hexadecimal][0] != "#") or (len(_dict[hexadecimal]) != 7):
            # doesn't start with # or  doesn't have 7 characters
            raise Exception("[write_user_config] one of the hexadecimals failed to validate")

        for char in (_dict[hexadecimal][1:]):
            if char not in valid_hex:
                raise Exception("[write_user_config] one of the hexadecimals failed to validate")

    return _dict


def write_user_preferences(json_dict: dict) -> None:
    """ perform validation and preprocessing, then write to user_config file """
    validated_dict = validate_all(json_dict)
    json_file = open(path, "w")
    dump(validated_dict, json_file)
    json_file.close()
