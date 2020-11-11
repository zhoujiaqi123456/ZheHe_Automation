from api.department_yml import DepartmentYml
from common.data_base import DataBase


class TestDepartmentYml:
    # 先实例化对象
    department_yml = DepartmentYml()

    def test_list_yml(self):
        r = self.department_yml.list("1")
        #断言
        assert r["errcode"] == 0
        assert r["department"][0]["name"] == "墨迹测试"
