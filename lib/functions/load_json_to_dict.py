""" load json file from path to dict """

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


def load_json_to_dict(path: str) -> dict:
    """ load the JSON file and performs postprocessing """
    json_file = open(path, "r")
    json_obj = json.load(json_file)

    json_obj = postprocess_booleans_read(json_obj)

    json_file.close()
    return json_obj
