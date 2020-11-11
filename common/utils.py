import json

from jsonpath import jsonpath


class Utils:
    @classmethod
    def format(cls, json_object):
        return json.dumps(json_object, indent=2,ensure_ascii=False)

    @classmethod
    def jsonpath(cls, json_object, expr):
        return jsonpath(json_object, expr)
    def printa(self):
        print("测试多继承")



if __name__ == '__main__':
    print(Utils.format({'qq':'22','aa':'ww'}))
