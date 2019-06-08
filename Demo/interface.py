# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-30 17:09
# @File    : interface.py
# @Software: PyCharm
import random
import string
from threading import Thread
import requests
import config


def random_materiel_name(length=3):
    random_str_list = [random.choice(string.digits + string.ascii_letters) for _ in range(length)]
    random_str = ''.join(random_str_list)
    return random_str


url_change = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/edit"
url_list = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/list"
url_add = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/add"
url_detail = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/detail"
url_delete = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/delete"

data_change = {
    "marketChannelId": "MESSAGE",
    "materielName": "并发后",
    "materielDescribe": "并发后",
    "useMaterielTemplate": "true",
    "materielLink": "https://www.baidu.com",
    "materielUnsubscribe": "true",
    "materielText": "据说人手都有一张信用卡？马上办卡，获取火箭粉丝专属特权，现在申请就送799元拉杆箱。点击<link>  回TD退订",
    "materielContent": "{\"desireAwake\":\"据说人手都有一张信用卡？\",\"corePoint\":\"马上办卡，获取火箭粉丝专属特权，\",\"rightsBenefits\":\"现在申请就送799元拉杆箱。\",\"link\":\"点击<link>\"}",
    "materielId": "MTR00002082"
}

data_list = {
    "pageNo": 1,
    "pageSize": 10
}

data_add = {
    "marketChannelId": "MESSAGE",
    # "marketChannelId": 1,
    "materielContent": '{"desireAwake":"想要提升学历、获取就业机会，","corePoint":"现参与推荐有礼活动，邀请好友购买保险最低可得52元，多邀多得","rightsBenefits":"还不快来参与。","link":"点击<link>"}',
    "materielDescribe": "interface_create",
    # "materielDescribe": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "materielLink": "https://www.taobao.com",
    # "materielLink": "abc",
    # "materielName": "物料-" + random_materiel_name(),
    "materielName": "aaaaaaaaaaaaaaaaaaaaaaaaa",
    "materielText": "想要提升学历、获取就业机会，现参与推荐有礼活动，邀请好友购买保险最低可得52元，多邀多得还不快来参与。点击<link>  回TD退订",
    "materielUnsubscribe": "true",
    "useMaterielTemplate": "true"
}

data_detail = {
    "materielId": "MTR00002060"
}

data_delete = {
    "materielId": "MTR00002072"
}

headers = {
    'cookie': config.cookie,
    'User-Agent': random.choice(config.agents)
}


def materiel(url, data=None):
    r = requests.post(url=url, json=data, headers=headers)
    res = r.json()
    print(res)


if __name__ == '__main__':
    # for _ in range(1):
    #     t = Thread(target=wuliao, args=(url_add, data_add,))
    #     t.start()
    materiel(url_list, data_list)
