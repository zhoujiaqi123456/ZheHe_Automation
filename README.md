# ZheHe_Automation
基于Pytest+request+Allure的接口自动化开源框架

----
### 模块类的设计

####api包存放接口代码
`wework.py` 作为公共参数这里是登陆token，用于接下来每个接口的入参数； app端接口测试
`test_department.py`

####common包存放公共方法
请求响应封装一：接口写在代码里面
`base_classes.py` 第一种封装request方法，可以支持多协议扩展（get\post\put）包含打印日志

数据库：
`data_base.py` 封装连接数据库，并且写了一些方法对比数据库和接口返回值

工具类：
`compare_data.py` 对比json 
`generation_casefile_php.py` 更加API文档自动生成yaml文件和测试业务代码
#####conf包
配置文件：
`config.ini` 存放项目多环境地址，项目多环境数据库连接信息等其他公用信息

#####api_yaml包：
存放 api接口信息

#####api包：
存放接口业务代码

#####TestCase包 存放自动化执行的测试用例
以项目模块来管理

#####Report包 存放自动化执行的报告；Allure
待完成

--