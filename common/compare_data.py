# -*- coding: utf-8 -*-
import json


class CompareData:
    @classmethod
    def read_json_from_file(cls, file_dir):

        '''
        读取.json文件内的json数据
        入参:file_dir为文件的绝对路径
        返回:.json文件里的json数据
        '''
        # print("当前路径 -> %s" %os.getcwd())
        with open(file_dir) as json_file:
            json_data = json.load(json_file)
        return json_data

    @classmethod
    def compare_json_value(cls, data, old_data, *ignore):
        # 统计丢失的数据
        cls.lost_data = []
        # 统计列表多出的数据个数
        cls.surplus_data = []
        # 统计不同的数据（不包括丢失的数据）
        cls.different_data = []
        cls.compare_dic_value(data, old_data, None, *ignore)
        result = {"lost_data": cls.lost_data, "surplus_data": cls.surplus_data, "different_data": cls.different_data}
        return result

    @classmethod
    def compare_dic_value(cls, data, old_data, dic_level, *ignore):
        for item in old_data:
            if dic_level == None:
                predic_level = item
            else:
                predic_level = dic_level + "." + item
            # print ("当前层级:" + predic_level)
            if predic_level not in ignore:
                newValue = data.get(item, -1)
                if newValue == -1:
                    cls.lost_data.append(predic_level)
                    print('*WARN*' + ' 丢失数据: ' + str(predic_level) + "--老接口数据为" + str(old_data[item]))
                else:
                    if isinstance(old_data[item], list):
                        # assert len(old_data[item]) == len(data[item])
                        print("是个list")
                        cls.compare_list_value(data[item], old_data[item], predic_level, *ignore)
                    elif isinstance(old_data[item], dict):
                        print("是个dic")
                        cls.compare_dic_value(data[item], old_data[item], predic_level, *ignore)
                    else:
                        cls.compare_basic_value(data[item], old_data[item], predic_level)

    @classmethod
    def compare_list_value(cls, data, old_data, dic_level, *ignore):
        # 新数据比老数据中列表多出的数据
        if len(data) > len(old_data):
            for i in range(len(old_data), len(data)):
                predic_level = dic_level + "." + str(i)
                if predic_level not in ignore:
                    cls.surplus_data.append(predic_level)
                    print('*WARN*' + ' 列表多出数据: ' + str(predic_level))

        for i in range(len(old_data)):
            predic_level = dic_level + "." + str(i)
            # print ("当前层级:" + predic_level)
            if i + 1 <= len(data):
                if predic_level not in ignore:
                    if isinstance(old_data[i], list):
                        assert len(old_data[i]) == len(data[i])
                        cls.compare_list_value(data[i], old_data[i], predic_level, *ignore)
                    elif isinstance(old_data[i], dict):
                        cls.compare_dic_value(data[i], old_data[i], predic_level, *ignore)
                    else:
                        cls.compare_basic_value(data[i], old_data[i], predic_level)
            else:
                # 新数据比老数据中列表丢失的数据
                cls.lost_data.append(predic_level)

    @classmethod
    def compare_basic_value(cls, data, old_data, dic_level):
        if data != old_data:
            print('*WARN*' + ' 数据不一致: ' + str(dic_level) + "--老接口数据为" + str(
                old_data) + "--新接口数据为" + str(data))
            cls.different_data.append(dic_level)

    @classmethod
    def compare_json_key(cls, data, old_data, *ignore):
        # 统计丢失的数据
        cls.lost_data = []
        # 统计列表多出的数据个数
        cls.surplus_data = []
        # 统计不同的数据（不包括丢失的数据）
        cls.different_data = []
        cls.compare_dic_key(data, old_data, None, *ignore)
        result = {"lost_data": cls.lost_data, "surplus_data": cls.surplus_data, "different_data": cls.different_data}
        return result

    @classmethod
    def compare_dic_key(cls, data, old_data, dic_level, *ignore):
        for item in old_data:
            if dic_level == None:
                predic_level = item
            else:
                predic_level = dic_level + "." + item
            # print ("当前层级:" + predic_level)
            if predic_level not in ignore:
                newValue = data.get(item, -1)
                if newValue == -1:
                    cls.lost_data.append(predic_level)
                    print('*WARN*' + ' 丢失数据: ' + str(predic_level) + "--老接口数据为" + str(old_data[item]))
                else:
                    if isinstance(old_data[item], list):
                        # assert len(old_data[item]) == len(data[item])
                        print("是个list")
                        cls.compare_list_key(data[item], old_data[item], predic_level, *ignore)
                    elif isinstance(old_data[item], dict):
                        print("是个dic")
                        cls.compare_dic_key(data[item], old_data[item], predic_level, *ignore)

    @classmethod
    def compare_list_key(cls, data, old_data, dic_level, *ignore):
        # 新数据比老数据中列表多出的数据
        if len(data) > len(old_data):
            for i in range(len(old_data), len(data)):
                predic_level = dic_level + "." + str(i)
                if predic_level not in ignore:
                    cls.surplus_data.append(predic_level)
                    print('*WARN*' + ' 列表多出数据: ' + str(predic_level))

        for i in range(len(old_data)):
            predic_level = dic_level + "." + str(i)
            # print ("当前层级:" + predic_level)
            if i + 1 <= len(data):
                if predic_level not in ignore:
                    if isinstance(old_data[i], list):
                        assert len(old_data[i]) == len(data[i])
                        cls.compare_list_key(data[i], old_data[i], predic_level, *ignore)
                    elif isinstance(old_data[i], dict):
                        cls.compare_dic_key(data[i], old_data[i], predic_level, *ignore)

            else:
                # 新数据比老数据中列表丢失的数据
                cls.lost_data.append(predic_level)

    @classmethod
    def json_to_dict(cls, injson):
        outdict = json.loads(injson)
        return outdict



if __name__ == '__main__':
    response = {
		"addresscall": "0571-89898989",
		"area": "浙江 杭州 临安市",
		"cityCode": "00975",
		"code": "01129913",
		"coordinate": "119.724733,30.233873"
	}

    result = {
		"addresscall": "0571-89898989",
		"area": "浙江 杭州 临安市",
		"cityCode": "00975",
		"code": "01129913",
		"coordinate": "119.724733,30.233873",
		"dateCreate": 1516012804000,
		"id": 214338,
		"isTest": 2,
		"name": "工具化测试店2",
		"nickname": "对内",
		"phone": "13777378840",
		"place": "五家渠市昌平区太平庄东一路16号",
		"provinceCode": "00974",
		"regionCode": "330185",
		"shopState": "rnning",
		"shortname": None,
		"storeType": None,
		"tgcChannel": 1,
		"type": "tgc_merchant",
		"walletAccontId": "200000952746"
	}
    print(CompareData().compare_json_value(response,result))