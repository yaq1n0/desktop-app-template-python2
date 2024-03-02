""" write to json file at path from dict """

# imports
import json


def preprocess_booleans_write(dict_from_json: dict) -> dict:
    """ process booleans from python boolean types before writing to JSON"""
    for e in dict_from_json:
        if dict_from_json[e] == True:
            dict_from_json[e] = "True"
        elif dict_from_json[e] == False:
            dict_from_json[e] = "False"

    return dict_from_json


def write_json_from_dict(path: str, json_obj: dict) -> None:
    """ perform some preprocessing and write to a JSON file """
    json_obj = preprocess_booleans_write(json_obj)

    json_file = open(path, "w")
    json.dump(json_obj, json_file)

    json_file.close()
