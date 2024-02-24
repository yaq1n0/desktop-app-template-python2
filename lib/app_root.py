"""this is where to store root variables and user preferences for the app."""

# imports
import json


def postprocess_booleans_read(dict_from_json: dict) -> dict:
    for e in dict_from_json:
        if dict_from_json[e] == "True":
            dict_from_json[e] = True
        elif dict_from_json[e] == "False":
            dict_from_json[e] = False

    return dict_from_json


def preprocess_booleans_write(dict_from_json: dict) -> dict:
    for e in dict_from_json:
        if dict_from_json[e] == True:
            dict_from_json[e] = "True"
        elif dict_from_json[e] == False:
            dict_from_json[e] = "False"

    return dict_from_json


def loadJSON(path: str) -> dict:
    json_file = open(path, "r")
    json_obj = json.load(json_file)

    json_obj = postprocess_booleans_read(json_obj)

    json_file.close()
    return json_obj


def writeJSON(path: str, json_obj: dict) -> None:
    json_obj = preprocess_booleans_write(json_obj)

    json_file = open(path, "w")
    json.dump(json_obj, json_file)

    json_file.close()


user_preferences = loadJSON("app_user_preferences.json")
default_preferences = loadJSON("app_default_preferences.json")

# generate font_size permutations automatically
font = user_preferences["font"]
font_size = user_preferences["font_size"]

font_sizes = {
    'Default': (font, font_size),
    'DefaultBold': (font, font_size, 'bold'),
    'Small': (font, int(round(font_size * 0.75, 0))),
    'SmallBold': (font, int(round(font_size * 0.75, 0)), 'bold'),
    'Large': (font, int(round(font_size * 1.25, 0))),
    'LargeBold': (font, int(round(font_size * 1.25, 0)), 'bold'),
    'ExtraLarge': (font, int(round(font_size * 1.50, 0))),
    'ExtraLargeBold': (font, int(round(font_size * 1.50, 0)), 'bold')
}

if __name__ == '__main__':
    """unit test for app_root.py"""

    print("testing loading json files")
    print("user preferences: " + str(user_preferences))
    print("default preferences: " + str(default_preferences))
    print("------------------------------------------")

    print("testing writing json files")
    test_preferences = default_preferences.copy()

    # invert dev and tooltips booleans
    test_preferences["dev"] = True
    test_preferences["tooltips"] = False
    # modify font to testing
    test_preferences["font"] = "testing"

    writeJSON("app_test_preferences.json", test_preferences)

    print("test preferences: " + str(loadJSON("app_test_preferences.json")))
    print("------------------------------------------")

    print("testing font_sizes permutations")
    for elem in font_sizes:
        print(elem, ':', font_sizes[elem])
