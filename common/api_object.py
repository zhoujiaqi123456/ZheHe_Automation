#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import logging
from requests import Request,Session
from requests_toolbelt.utils import dump
from urllib.parse import unquote

class ApiObject(object):

    method = ""
    url = ""
    params = {}
    headers = {}
    data = {}
    json = {}

    def run(self):
        """
        访问 get 和 post 接口
        :param method：请求方法
        :param url：URL地址
        :param params：参数放到URL里面传递，
        :param data：在form表单中传递参数
        :param json：json 格式
        """
        s = Session()
        # s.verify = False
        # s.headers = {'Content-Type': 'application/json; charset=utf-8'}
        request = Request(method=self.method, url=self.url, params=self.params, data=self.data, headers=self.headers)
        prepare = s.prepare_request(request)
        resp = s.send(prepare)
        data = dump.dump_all(resp)
        print(unquote(data.decode('utf-8')))
        return resp.json()




if __name__ == '__main__':
    # json = {"name": "测试python88", "parentid": 1, "order": 1, "id": 3336}
    # params = {"access_token": "nuyR-E1-77rlQDVNoWrpQCk7YQrAq7nhH2nADV-t-qLabxqYYfV0ojz0KCCqya4YVkFnD8Le2gvDCHrzT4ip-I93mhbTBEnrichD-WiQXS6G5RC_yHlYleyiLznDSVXXFEJAuK_sG2wWDTv_AM_L4Pg8e21ZNQekhPJ5zINsx0FO3rKi85mNcirxaYQZuv-f3w34lDziG5O2CPjMGexSQQ"}
    # headers = {'content-type': 'application/json; charset=utf-8'}

    # apiObject = ApiObject()
    # apiObject.url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    # apiObject.method = "post"
    # apiObject.params = {"access_token": "lNkpiH61l2El8_3WNiw3U716sShLlAOapFPxuG_gRlFvV3EdlmmsdTRx-f_DeS8xW6XFXDTvFSXoyCEbeg9V1DCvwLKQ5f_esVXcz1eOoD5g4Nidye_f78LSj4fLnhv7c3JBRI8F1yWl4L6gkKbSda2PpAnIw8WMrRPPCHwSTtbonch3vm5VpDdppbWbsqCWpqmi_s88kbnrmiH3MSmEPg"}
    # apiObject.headers={'content-type': 'application/json; charset=utf-8'}
    # apiObject.json={"name": "ce11", "parentid": 1, "order": 1, "id": 3336}
    # print(apiObject.run().json())

    apiObject = ApiObject()
    apiObject.url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    apiObject.method = "get"
    apiObject.params = {"access_token": "lNkpiH61l2El8_3WNiw3U716sShLlAOapFPxuG_gRlFvV3EdlmmsdTRx-f_DeS8xW6XFXDTvFSXoyCEbeg9V1DCvwLKQ5f_esVXcz1eOoD5g4Nidye_f78LSj4fLnhv7c3JBRI8F1yWl4L6gkKbSda2PpAnIw8WMrRPPCHwSTtbonch3vm5VpDdppbWbsqCWpqmi_s88kbnrmiH3MSmEPg"}
    print(apiObject.run())

