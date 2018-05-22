import json


def read_json_file(path_to_file):
    """ Import datas in json file. """
    with open(path_to_file) as f:
        db_config = json.load(f)
    return db_config
