import os
import json
import requests
import pydash
from . import CronJob
from . import http_headers


class CherrySwapWhiteTokenList(CronJob):
    """
    Site: https://www.cherryswap.net
    """
    def __init__(self):
        super(CherrySwapWhiteTokenList, self).__init__()
        self.token_list_save_file = './data/cherrySwapWhiteTokenList.json'
        self.token_json_url = 'https://www.cherryswap.net/swapimages/json/t3/cherryswap.json'

    def load_local_token_list(self) -> list:
        t = os.path.isfile(self.token_list_save_file)
        if not t:
            return []
        with open(self.token_list_save_file, 'r') as f:
            return json.load(f)

    def load_remote_token_list(self) -> list:
        response = requests.get(self.token_json_url, headers=http_headers)
        if response.status_code != 200:
            raise requests.RequestException
        return response.json()['tokens']

    def check_has_new_coin(self, local_token_list: list, remote_token_list: list) -> list:
        """
        :param local_token_list, source data
        :param remote_token_list, source data
        :returns: list<tokenAddress>
        """
        t1 = pydash.map_(local_token_list, 'address')
        t2 = pydash.map_(remote_token_list, 'address')
        r = set(t2) - set(t1)
        return list(r)
    
    def save_token_list(self, token_list: list):
        with open(self.token_list_save_file, 'w') as f:
            f.write(json.dumps(token_list))
            
    
    def generate_message(self, new_tokens: list, source_token_list: list) -> str:
        tokens = []
        for token_address in new_tokens:
            s = pydash.find(source_token_list, { "address": token_address })
            if s:
                tokens.append(s)
        msg = '**Cherry Swap White Token List New Coin** \n\n'
        for item in tokens:
            msg += f"symbol: {item['symbol']}, address: {item['address']} \n\n"
        return msg
    
    def run(self):
        local_token_list = self.load_local_token_list()
        remote_token_list = self.load_remote_token_list()
        if len(local_token_list) == 0:
            self.save_token_list(remote_token_list)
            return
        new_tokens = self.check_has_new_coin(local_token_list, remote_token_list)
        if len(new_tokens) > 0:
            msg = self.generate_message(new_tokens, remote_token_list)
            self.send_message(msg)
        self.save_token_list(remote_token_list)