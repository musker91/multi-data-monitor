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

class KSwapWhiteTokenList(CronJob):
    """
    Site: https://app.kswap.finance
    """
    def __init__(self):
        super(KSwapWhiteTokenList, self).__init__()
        self.token_list_save_file = './data/kSwapWhiteTokenList.json'
        self.token_json_url = 'https://static.kswap.finance/tokenlist/kswap-hosted-list.json'

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
        msg = '**KSwap White Token List New Coin** \n\n'
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

class GateIoAllMarkets(CronJob):
    """
    Site: https://gate.io
    """
    def __init__(self):
        super(GateIoAllMarkets, self).__init__()
        self.market_list_save_file = './data/gateIoAllMarkets.json'
        self.market_json_url = 'https://data.gateapi.io/api2/1/marketlist'

    def load_local_market_list(self) -> list:
        t = os.path.isfile(self.market_list_save_file)
        if not t:
            return []
        with open(self.market_list_save_file, 'r') as f:
            return json.load(f)

    def load_remote_market_list(self) -> list:
        response = requests.get(self.market_json_url, headers=http_headers)
        if response.status_code != 200:
            raise requests.RequestException
        return response.json()['data']

    def check_has_new_coin(self, local_market_list: list, remote_market_list: list) -> list:
        """
        :param local_market_list, source data
        :param remote_market_list, source data
        :returns: list<marketAddress>
        """
        t1 = pydash.map_(local_market_list, 'pair')
        t2 = pydash.map_(remote_market_list, 'pair')
        r = set(t2) - set(t1)
        return list(r)
    
    def save_market_list(self, market_list: list):
        with open(self.market_list_save_file, 'w') as f:
            f.write(json.dumps(market_list, indent=2))
            
    
    def generate_message(self, new_pairs: list, source_market_list: list) -> str:
        markets = []
        for pair in new_pairs:
            s = pydash.find(source_market_list, { "pair": pair })
            if s:
                markets.append(s)
        msg = '**Gate.io Add New Market Pair** \n\n'
        for item in markets:
            msg += f"pair: {item['pair']}, name: {item['name']}, symbol: {item['symbol']} \n\n"
        return msg
    
    def run(self):
        local_market_list = self.load_local_market_list()
        remote_market_list = self.load_remote_market_list()
        if len(local_market_list) == 0:
            self.save_market_list(remote_market_list)
            return
        new_pairs = self.check_has_new_coin(local_market_list, remote_market_list)
        if len(new_pairs) > 0:
            msg = self.generate_message(new_pairs, remote_market_list)
            self.send_message(msg)
        self.save_market_list(remote_market_list)