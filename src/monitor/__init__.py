import json
import requests
from config import config as serviceConfig

http_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}

class CronJob(object):
    def __init__(self):
        pass
    
    def _dingding_msg_template(self, msg: str, title: str = '') -> str:
        return {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": msg,
            },
            "at": {
                "atMobiles": [],
                "isAtAll": False
            }
        }
    
    
    def _send_dingding_msg(self, msg: str, token: str, title: str = ''):
        msg_template_msg = self._dingding_msg_template(msg, title)
        json_data = json.dumps(msg_template_msg).encode(encoding='utf-8')
        url = f'{serviceConfig.DINGDING_APi}{token}'
        headers = {
            **http_headers,
            "Content-Type": "application/json"
        }
        requests.post(url, data=json_data, headers=headers)

    
    def send_message(self, msg: str):
        for item in serviceConfig.DINGDING_RECIVE_LIST:
            self._send_dingding_msg(msg, item['token'], item['title'])


    def run(self):
        """
        Cron Run Entry
        """
        pass
