# -*- coding: utf-8 -*-
import uuid
import string
import random
import requests
import logging
from conf.config import Config
from requests_toolbelt.utils import dump
from common.utils import Utils
from urllib.parse import unquote
import os
import yaml
import pystache
from common.api_object import ApiObject



"""
该类为基类；后续 不同模块业务需要继承；该类包含公用的方法
"""
class BaseClasses(object):

    __root_path = ""

    def request(self, file_name, context):
        """
        :param file_name: yml文件名称
        :param context: 要替换的参数，字典类型
        :return: 发起请求
        """
        self.__root_path = os.path.dirname(os.path.abspath('.')) + '/conf/'
        print(self.__root_path+file_name)
        # self.__root_path = os.getcwd() + '/conf/'
        apiObject = self.__read_template(self.__root_path + file_name, context)
        return apiObject.run()

    def __read_template(self, file_path, context):
        file_content = ""
        with open(file_path, 'r') as f:
            file_content = f.read()
        api_request = ApiObject()
        api_request.__dict__ = yaml.load(self.__template_render(file_content, context), Loader=yaml.FullLoader)
        return api_request

    def __template_render(self, template, context):
        return pystache.render(template, context)

    @classmethod
    def verbose(cls, json_object):
        print(Utils.format(json_object))
        # cls.printer.pprint(json_object)

    @classmethod
    def jsonpath(cls, expr):
        return Utils.jsonpath(cls.json_data, expr)

    def jsonpath(self, expr):
        return Utils.jsonpath(self.json_data, expr)



    @classmethod
    def request_api(cls, method, url, params =None, data=None, json=None, headers =None, **kwargs):
        """
        访问 get 和 post 接口
        :param method：请求方法
        :param url：URL地址
        :param params：参数放到URL里面传递，
        :param data：在form表单中传递参数
        :param json：json 格式
        """
        #         upper 转换成大写
        if method.upper() == 'GET':
            """ 发送get请求
                        params 传递参数就是放到URL里面传递
                        data 在form表单中传递参数 """
            try:
                res = requests.get(url, params=params, **kwargs)
                res.encoding = 'utf-8'
                data = dump.dump_all(res)
                print(unquote(data.decode('utf-8')))

            except Exception:
                # 记录异常到日志
                logging.info('访问get请求不成功')
        elif method.upper() == 'POST':
            """ 发送post请求 """
            try:
                res = requests.post(url, params=params, data=data, json=json, headers=headers, **kwargs)
                res.encoding = 'utf-8'
                data = dump.dump_all(res)
                print(unquote(data.decode('utf-8')))
            except Exception:
                # 记录异常到日志
                logging.info('访问post请求不成功')
        elif method.upper() == 'DELETE':
            try:
                res = requests.delete(url,params=params,**kwargs)
                res.encoding = 'utf-8'
                data = dump.dump_all(res)
                print(unquote(data.decode('utf-8')))
            except Exception:
                logging.info('访问delete请求不成功')
        elif method.upper() == 'PUT':
            try:
                res = requests.put(url, params=params, data=data, json=json, headers=headers, **kwargs)
                res.encoding = 'utf-8'
                data = dump.dump_all(res)
                print(unquote(data.decode('utf-8')))
            except Exception:
                logging.info('访问put请求不成功')
        return res.json()

    @classmethod
    def get_config(cls, sectionname, key):
        """获取配置文件内，对应sectionname内，key对应的value"""
        cf = Config().cf
        var = cf.get(sectionname, key)
        return var

    @classmethod
    def random_uuid(cls):
        '''随机生成uuid'''
        data = uuid.uuid1()
        return str(data)

    @classmethod
    def random_num(cls):
        '''随机生成0-100以内的数字'''
        data = random.randint(0,100)
        return str(data)

    @classmethod
    def random_email(cls):
        '''随机生成邮件地址'''
        # 生成邮件头
        rd_name = []
        rd_name.append(string.digits)
        rd_name.append(string.ascii_letters)
        rd_name = "".join(rd_name)
        random_email_header = "".join(random.choice(rd_name) for i in range(5))

        # 邮件后缀
        s = ['@163.com', '@qq.com', '@sina.com', '@126.com']
        email_adr = random.choice(s)
        email = "{}{}".format(random_email_header, email_adr)
        return email




if __name__ == '__main__':
    BaseClasses().request("api.yml", {"id": 1, "access_token": "lNkpiH61l2El8_3WNiw3U716sShLlAOapFPxuG_gRlFvV3EdlmmsdTRx-f_DeS8xW6XFXDTvFSXoyCEbeg9V1DCvwLKQ5f_esVXcz1eOoD5g4Nidye_f78LSj4fLnhv7c3JBRI8F1yWl4L6gkKbSda2PpAnIw8WMrRPPCHwSTtbonch3vm5VpDdppbWbsqCWpqmi_s88kbnrmiH3MSmEPg"})

    # json = {"name": "测试python88", "parentid": 1, "order": 1, "id": 836}
    # params = {
    #     "access_token": "nuyR-E1-77rlQDVNoWrpQCk7YQrAq7nhH2nADV-t-qLabxqYYfV0ojz0KCCqya4YVkFnD8Le2gvDCHrzT4ip-I93mhbTBEnrichD-WiQXS6G5RC_yHlYleyiLznDSVXXFEJAuK_sG2wWDTv_AM_L4Pg8e21ZNQekhPJ5zINsx0FO3rKi85mNcirxaYQZuv-f3w34lDziG5O2CPjMGexSQQ"}
    # headers = {'content-type':'application/json; charset=utf-8'}
    # print(BaseClasses().request_api("post", "https://qyapi.weixin.qq.com/cgi-bin/department/create", params, json, headers))

    # print(Config().get_config('MYSQL', 'USER'))

    # print(BaseClasses().random_num())




