
import requests
import json
import random
import time
import re

def chat(authorization, chanel_id, content):

    proxy = '127.0.0.1:10809'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    print(proxies)
    # 伪装头
    header = {
        "Authorization": authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    print(header)
    # 整理发送的内容、生成nonce
    msg = {
        "content": content,
        "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),  # 923802142370693120 923802484009336832
        "tts": False
    }
    print(msg)
    # 拼接频道地址
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(chanel_id)
    print(url)
    res = requests.post(url=url, headers=header, data=json.dumps(msg), proxies=proxies, timeout=5)
    print(res.status_code)
    print(res.content)


if __name__ == '__main__':
    while True:
        try:
            chat()
            sleeptime = random.randrange(5, 10)
            print(sleeptime)
            time.sleep(sleeptime)
        except:
            pass
        continue
