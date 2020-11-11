import json
import os
import yaml
import shutil
import re

def read_json(case_path, module_name):
    root_dir = os.path.dirname(os.path.abspath('.'))
    # print("根目录为" + root_dir)
    case_dir = root_dir + case_path
    # print("读取的配置文件为" + case_dir)
    date = {}
    with open(case_dir, "r") as f:
        data = json.load(f)

    interfacePoList = []
    for i in data["api"]:
        interfacePo = InterfacePo()
        interfacePo.method = i["type"]
        interfacePo.url = i["url"]
        if 'parameter' in i.keys():
            interfacePo.data = get_params(i['parameter']['fields']['Parameter'])
        interfacePo.groupTitle = i['groupTitle']
        interfacePo.name = i['name']
        interfacePo.title=i['title']
        interfacePoList.append(interfacePo)

    write_file(grouping(distinct(interfacePoList)), module_name)


def write_file(total_data, module_name):
    '''
    :param total_data: 分组后的字典格式的数据
    :param module_name: 模块名
    :return: None
    '''

    #取出需要的数据，并整理成list
    data = []
    if not module_name:
        for i in total_data.keys():
            for j in total_data[i]:
                data.append(j)
    else:
        for i in total_data[module_name]:
            data.append(i)

    #开始写文件
    for i in data:
        # 1. 判断文件夹是否存在，存在则直接写yaml文件，不存在则新建文件夹
        # 方法2. 不判断文件夹是否存在，捕获文件夹重复异常，忽略该异常，进行下一步操作
        yaml_path = os.path.dirname(os.path.abspath('.')) + '/apijson_yaml'
        os.chdir(yaml_path)
        try:
            os.mkdir(yaml_path + '/' + i['groupTitle'])
        except IOError:
            print("yaml模块包已经存在")
        group_title = i['groupTitle']
        name = i['name']
        i.pop('groupTitle')
        i.pop('name')
        write_yaml(yaml_path + '/' + group_title + '/' + name + ".yaml", i)
        api_path = os.path.dirname(os.path.abspath('.')) + '/apijson'
        os.chdir(api_path)
        write_api_model(api_path + '/' + group_title+'.py', name, i['data'])
        test_api_path = os.path.dirname(os.path.abspath('.')) + '/testcases'
        os.chdir(test_api_path)
        try:
            os.mkdir(test_api_path + '/' + group_title)
        except IOError:
            print("测试模块已经存在")
        write_test_api(test_api_path + '/' + group_title +'/'+ 'test'+hump_to_underline(name)+ '.py', group_title, name)

def grouping(total_data):
    data = {}
    for i in total_data:
        group_name = i.groupTitle
        if group_name in data:
            group_data = data[group_name]
            group_data.append(i.__dict__)
            data.update({group_name : group_data})
        else:
            data.update({group_name : [i.__dict__]})
    return data

#去除数据中重复的接口
def distinct(total_data):
    data = {}
    for i in total_data:
        data.update({i.name:i})
    result = []
    for i in data.keys():
        result.append(data[i])
    return result

def get_params(params):
    data = {}
    for i in params:
        key = i['field']
        value = "{{" + key + "}}"
        data.update({key:value})
    return data

def write_yaml(dir, interfacePo):
    with open(dir, "w", encoding="utf-8") as f:
        yaml.dump(interfacePo, f, allow_unicode=True)


def write_api_model(dir, file_name, params):
    four_blank = '    '
    with open(dir, "a", encoding="utf-8") as f:
        # modelparam = io.StringIO()
        if params:
            f.writelines("\n" + "def" +" " + file_name +
                         "(" + "self," + str(params) + "):" + "\n" + four_blank + "self.json_data = self.request(" +"'"
                         + file_name + ".yaml' ," + str(params) + ")" + "\n" + four_blank +
                         "print(self.verbose(self.json_data))" + "\n" + four_blank + "return self.json_data\n\n")
        else:
            f.writelines("\n" + "def" +" " + file_name +
                         "(" + "self" + "):" + "\n" + four_blank + "self.json_data = self.request(" +"'" +
                         file_name + ".yaml'" + ")" + "\n" + four_blank +
                         "print(self.verbose(self.json_data))" + "\n" + four_blank + "return self.json_data\n\n")
    f.close()

def write_test_api(dir, module_name ,file_name):
    four_blank = '    '
    with open(dir, "a+", encoding="utf-8") as f:
        # f.writelines("\n" + "def" + " "+"test_" + str(file_name))
        f.writelines("\n" + "def"+" "+"test_" + str(file_name) +
                     "(" + "self" + "):" + "\n" + four_blank + "response=self." + module_name + "." + file_name + "()"
                     "\n" +four_blank+ "assert"+" "+"response"+"["+"'code'"+"]"+"==200")
        f.close()



def hump_to_underline(camelCaps, separator="_"):
    pattern = re.compile(r'([A-Z]{1})')
    sub = re.sub(pattern, separator+r'\1', camelCaps).lower()
    return sub

class InterfacePo:
    title=''
    name = ""
    method = ""
    url = ""
    params = None
    headers = None
    data = None
    json = None
    groupTitle = ""



if __name__ == '__main__':
    # case_path='/conf/response.json'
    # read_json(case_path, '后台运单管理')
    a="{'name': '测试岗位2221', 'nameEn': 'testjob', 'level': '0', 'code': '78d3648b0aa448909792cbf91e8180f5'}"
    print(hump_to_underline(a))