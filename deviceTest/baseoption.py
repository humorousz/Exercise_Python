import requests
import json

#
# 一些基本操作的集合
#
url_test = "http://kdev.test.gifshow.com"
url_online = "https://kdev.corp.kuaishou.com"
path_proxy = "/api/mock/longConn/open/uiAutoTest/updateProxySetting"

app_package = "com.smile.gifmaker"
app_home_activity = "com.yxcorp.gifshow.HomeActivity"

headers = {"content-type": "application/json",
           "userToken": "20001_894222c98d3a8f3dbdf538249393971b"}

body = {
    "bizId": 1,
    "envType": 3,
    "remoteIp": "172.29.67.177",
    "remotePort": "3209",
    "status": 1,
    "model": 1,
    "envId": 3,
    "userName": "zhangzhiquan03"}


class BaseOption:
    @staticmethod
    def open_kwai_app(device):
        device.app_start(app_package, app_home_activity)


class BaseKDevOption:
    @staticmethod
    def send_post(url, header, data):
        print(header)
        print(json.dumps(data))
        return requests.post(url=url, headers=header, data=json.dumps(data))

    def close_env(self):
        body['status'] = 0
        return self.send_post(url_online + path_proxy, headers, body)

    def open_staging_env(self):
        body['status'] = 1
        body['envType'] = 3
        return self.send_post(url_online + path_proxy, headers, body)


if __name__ == '__main__':
    kDevOption = BaseKDevOption()
    kDevOption.close_env()
    kDevOption.open_staging_env()
