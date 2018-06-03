import json

import mysitedj2_0.settings.base as s_base


def read_json_file(path_to_file):
    """ Import datas in json file. """
    with open(path_to_file) as f:
        db_config = json.load(s_base.REPO_DIR + f)
    return db_config
