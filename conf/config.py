import os
import threading
import configparser

class Config:
    """创建配置文件单例类"""

    _instance_lock = threading.Lock()

    def __init__(self):
        global root_dir, case_dir
        root_dir = os.path.dirname(os.path.abspath('.'))
        print("根目录为"+root_dir)
        case_dir = root_dir + '/conf/config.ini'
        print("读取的配置文件为"+case_dir)
        self.cf = configparser.ConfigParser()
        rs = self.cf.read(case_dir)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Config, "_instance"):
            with Config._instance_lock:
                if not hasattr(Config, "_instance"):
                    Config._instance = object.__new__(cls)
        return Config._instance

    def get_config(self, sectionname, key):
        """获取配置文件内，对应sectionname内，key对应的value"""
        cf = Config().cf
        var = cf.get(sectionname, key)
        return var

if __name__ == '__main__':
    print(Config().get_config('MYSQL', 'USER'))

