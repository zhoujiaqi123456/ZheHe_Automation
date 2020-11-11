
import requests

from common.base_classes import BaseClasses


class WeWork(BaseClasses):
    corpid = "ww3d37f5e21f626c79"
    agentid = "1000002"
    contact_secret = "57GWfW1EFQfwiyAU3GNBYbmS7qsNqQIv9X_Pc0v-T98"
    access_token_contact = None


    @classmethod
    def get_access_token(cls):
        if cls.access_token_contact == None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.contact_secret}).json()
            print("获取token作为参数")
            cls.verbose(r)
            cls.access_token_contact = r["access_token"]
        return WeWork.access_token_contact

if __name__ == '__main__':
    print(WeWork.get_access_token())



