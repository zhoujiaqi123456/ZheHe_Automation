# -*- coding:utf-8 -*-
import os,io
import re
import time
import shutil
import yaml
import api_yaml
import api


def automatic_generation_case(case_path):
    global root_dir, case_dir
    root_dir = os.path.dirname(os.path.abspath('.'))
    # print("根目录为" + root_dir)
    case_dir = root_dir + case_path
    # print("读取的配置文件为" + case_dir)

    lines = []
    with open(case_dir) as f:
        lines = f.readlines()
        #index为模块名的行数
    index = []
    module = []
    module_name = []

    # 获取每一块的开始下标
    for i in range(len(lines)):
        if len(lines[i]) > 2:
            if (lines[i][0] == '#') & (lines[i][1] != '#'):
                module_name.append(lines[i].replace('#', '').strip())
                index.append(i)

    # 分块截取，i为多少模块数
    for i in range(len(index)):
        if len(index) == (i+1):
            module.append(lines[index[i]:])
        else:
            module.append(lines[index[i]:index[i + 1]])
#module=[[模块1内容】，【模块2内容】，【模块3内容】]； i为多少个模块； j为单个模块长度
    interface_index = []
    for i in range(len(module)):
        index_tmp = []
        for j in range(len(module[i])):
            if module[i][j][0:2] == '##':
                index_tmp.append(j)
        interface_index.append(index_tmp)

    total_interface_content = []
    for i in range(len(module)):
        total_interface_content.append(get_interface_content(interface_index[i], module[i]))

    # 循环写yaml文件
    for i in range(len(total_interface_content)):
        yaml_path = os.path.dirname(os.path.abspath('.'))+'/api_yaml'
        os.chdir(yaml_path)
        files = os.listdir(yaml_path)
        for item in files:
                if os.path.isdir(item):
                    if os.path.exists(yaml_path + '/' + module_name[i]):
                        shutil.rmtree(yaml_path + '/' + module_name[i])
                        os.mkdir(yaml_path + '/' + module_name[i])
                        for j in range(len(total_interface_content[i])):
                            interfacePo = get_interfacePo(total_interface_content[i][j])
                            file_name = interfacePo.name.replace("/", "_")
                            yaml_dict = interfacePo.__dict__
                            yaml_dict.pop('name')
                            if len(yaml_dict.get('params')) == 0:
                                yaml_dict.pop('params')
                            write_yaml(yaml_path + '/' + module_name[i] + '/' + yaml_dict.get('method').lower()
                                       +yaml_dict.get('url').replace('/', '_') + ".yaml", yaml_dict)
                    else:
                        os.mkdir(module_name[i])
                        for j in range(len(total_interface_content[i])):
                            interfacePo = get_interfacePo(total_interface_content[i][j])
                            file_name = interfacePo.name.replace("/", "_")
                            yaml_dict = interfacePo.__dict__
                            yaml_dict.pop('name')
                            if len(yaml_dict.get('params')) == 0:
                                yaml_dict.pop('params')
                            write_yaml(yaml_path + '/' + module_name[i] + '/' + yaml_dict.get('method').lower()
                                       +yaml_dict.get('url').replace('/', '_') + ".yaml", yaml_dict)
    # 循环写测试代码文件
    for i in range(len(total_interface_content)):
        test_path = os.path.dirname(os.path.abspath('.'))+'/testcases'
        os.chdir(test_path)
        files = os.listdir(test_path)
        for item in files:
                if os.path.isdir(item):
                    if os.path.exists(test_path + '/' + module_name[i]):
                        shutil.rmtree(test_path + '/' + module_name[i])
                        os.mkdir(test_path + '/' + module_name[i])
                        for j in range(len(total_interface_content[i])):
                            interfacePo = get_interfacePo(total_interface_content[i][j])
                            file_name = interfacePo.name.replace("/", "_")
                            yaml_dict = interfacePo.__dict__
                            yaml_dict.pop('name')
                            if len(yaml_dict.get('params')) == 0:
                                yaml_dict.pop('params')
                            write_test_api(test_path + '/' + module_name[i] + '/' + 'test'+yaml_dict.get('url').replace('/', '_') +
                                            '_'+yaml_dict.get('method').lower() + ".py", module_name[i], yaml_dict.get('method').lower() +yaml_dict.get('url').replace('/', '_'))
                            # write_test_api(test_path + '/' + module_name[i] + '/' + file_name + ".py",module_name[i]
                            #                , file_name)
                    else:
                        os.mkdir(module_name[i])
                        for j in range(len(total_interface_content[i])):
                            interfacePo = get_interfacePo(total_interface_content[i][j])
                            file_name = interfacePo.name.replace("/", "_")
                            yaml_dict = interfacePo.__dict__
                            yaml_dict.pop('name')
                            if len(yaml_dict.get('params')) == 0:
                                yaml_dict.pop('params')
                            write_test_api(test_path + '/' + module_name[i] + '/' + yaml_dict.get('url') +
                                           yaml_dict.get('method') + ".py", module_name[i], yaml_dict.get('method')
                                           .lower() +yaml_dict.get('url').replace('/', '_'))
                            # write_test_api(test_path + '/' + module_name[i] + '/' + file_name + ".py",module_name[i]
                            #                , yaml_dict.get('params'))
    # 循环写业务代码文件
    for i in range(len(total_interface_content)):
        print(i)
        print("总的total_interface_content {0}".format(len(total_interface_content)))
        api_path = os.path.dirname(os.path.abspath('.')) + '/api'
        files = os.listdir(api_path)
        print("files:{0}".format(files))
        for item in files:
            # if os.path.isfile(item):
            if os.path.exists(api_path + '/' + module_name[i]+'.py'):
                os.remove(api_path + '/' + module_name[i]+'.py')
                for j in range(len(total_interface_content[i])):
                    interfacePo = get_interfacePo(total_interface_content[i][j])
                    file_name = interfacePo.name.replace("/", "_")
                    yaml_dict = interfacePo.__dict__
                    write_api_model(api_path + '/' + module_name[i]+'.py', yaml_dict.get('method').lower() +
                                    yaml_dict.get('url').replace('/', '_'), yaml_dict.get('params'))



            else:
                for j in range(len(total_interface_content[i])):
                    interfacePo = get_interfacePo(total_interface_content[i][j])
                    file_name = interfacePo.name.replace("/", "_")
                    yaml_dict = interfacePo.__dict__
                    write_api_model(api_path + '/' + module_name[i] + '.py', yaml_dict.get('method').lower() +
                                    yaml_dict.get('url').replace('/', '_'), yaml_dict.get('params'))


def get_interface_content(interface_index, module_content):
    '''
    :param interface_index:  接口在对应模块中所在的行数
    :param module_content:   模块的数据
    :return: 返回分割后的每个接口组成的数组
    '''
    interface_content = []
    for i in range(len(interface_index)):
        if len(interface_index) == (i + 1):
            interface_content.append(module_content[interface_index[i]:])
        else:
            interface_content.append(module_content[interface_index[i]:interface_index[i+1]])
    return interface_content


def get_interfacePo(interface_content):
    interfacePo = InterfacePo()
    params_line_index = ''
    for i in range(len(interface_content)):
        line = interface_content[i]
        #接口名称
        if line[0:2] == '##':
            interfacePo.name = line[3:].strip()
        #接口url
        if '**接口地址**' in line:
            interfacePo.url = line.split('`')[1].strip().replace('{', '{{').replace('}', '}}')
        #请求方式
        if '**请求方式**' in line:
            interfacePo.method = line.split('`')[1].strip()
    interfacePo.params = get_request_params(interface_content)
    return interfacePo



def get_request_params(interface_content):

    begin_index = 9999999
    end_index = 0
    for i in range(len(interface_content)):
        if len(interface_content[i]) > 2:
            if '**请求参数**' in interface_content[i]:
                begin_index = i
            if (i > begin_index) & (interface_content[i][0:2] == '**'):
                end_index = i
                break

    #获取所有参数行内容
    params_content = interface_content[begin_index:end_index][4:-1]

    params = {}
    for line in params_content:
        params_key = ''
        params_value = ''
        if line.split('|')[3].strip() == 'query':
            params_key = line.split('|')[1].strip()
            params_value = '{{' + params_key + '}}'
            params.update({params_key:params_value})

    return params


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



class InterfacePo:
    name = ""
    desc = ""
    method = ""
    url = ""
    params = None
    headers = None
    data = None
    json = None

if __name__ == '__main__':
    # with open("/Users/zhehe/ZheHe_Automation/api/auth-controller.py") as f:
    #     s = io.StringIO()
    #     s.write("from common.base_classes import BaseClasses\n")
    #
    #     # print(s.getvalue())
    #     f.write(s.getvalue())
    #     s.flush()
    #     f.close()

    automatic_generation_case('/conf/guanya.md')
    # for i in range(1):
    #     for j in range(3):
    #         print("打印个数")
    #         with open("/Users/zhehe/ZheHe_Automation/api/auth_controller.py","a", encoding="utf-8") as f:
    #             f.write("111\n")
    #             f.write("222\n")
    #             f.close()



