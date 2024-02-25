""" app_root.py : this is where to store root variables for the app as well as manipulates the JSON files used to
store program configuration """

# imports
import json


def postprocess_booleans_read(dict_from_json: dict) -> dict:
    """ process boolean strings into python boolean types after reading from JSON """
    for e in dict_from_json:
        if dict_from_json[e] == "True":
            dict_from_json[e] = True
        elif dict_from_json[e] == "False":
            dict_from_json[e] = False

    return dict_from_json


def preprocess_booleans_write(dict_from_json: dict) -> dict:
    """ process booleans from python boolean types before writing to JSON"""
    for e in dict_from_json:
        if dict_from_json[e] == True:
            dict_from_json[e] = "True"
        elif dict_from_json[e] == False:
            dict_from_json[e] = "False"

    return dict_from_json


def loadJSON(path: str) -> dict:
    """ load the JSON file and performs postprocessing """
    json_file = open(path, "r")
    json_obj = json.load(json_file)

    json_obj = postprocess_booleans_read(json_obj)

    json_file.close()
    return json_obj


def writeJSON(path: str, json_obj: dict) -> None:
    """ perform some preprocessing and write to a JSON file """
    json_obj = preprocess_booleans_write(json_obj)

    json_file = open(path, "w")
    json.dump(json_obj, json_file)

    json_file.close()


# load user_preferences and default_preferences
user_preferences = loadJSON("lib/app_user_preferences.json")
default_preferences = loadJSON("lib/app_default_preferences.json")

# generate font permutations automatically
font = user_preferences["font"]
font_size = user_preferences["font_size"]

# global font permutations dictionary
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

if __name__ == '__main__':
    """unit test for app_root.py"""

    print("testing loading json files")
    print("user preferences: " + str(user_preferences))
    print("default preferences: " + str(default_preferences))
    print("------------------------------------------")

    print("testing font_sizes permutations")
    for elem in fonts:
        print(elem, ':', fonts[elem])
