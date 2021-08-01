import os
import json
from . import CronJob


class CherrySwapWhiteTokenList(CronJob):
    def __init__(self):
        super(CherrySwapWhiteTokenList, self).__init__()
        self.token_list_save_file = '../data/cherrySwapWhiteTokenList.json'
        self.token_json_url = 'https://www.cherryswap.net/swapimages/json/t3/cherryswap.json'

    def load_local_token_list(self) -> list:
        t = os.path.isfile(self.token_list_save_file)
        if not t:
            return []
        with open('r', self.token_list_save_file) as f:
            return json.load(f)

    def get_token_list(self) -> list:
        pass

    def check_has_new_coin(self):
        pass
    
    def run(self):
        pass
