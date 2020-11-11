from datetime import datetime
from api.department import Department
from common.data_base import DataBase
import pytest



class TestAll:
    # # 先实例化对象
    department = Department()
    # db = DataBase(department.get_config("MYSQL", "HOST"), department.get_config("MYSQL", "PORT"),
    #               department.get_config("MYSQL", "USER"), department.get_config("MYSQL", "PASSWORD"),
    #               department.get_config("MYSQL", "DATABASE"))

    def test_all(self):
        #先新增部门
        name = "集成测试部门" + str(datetime.now().second)
        r = self.department.create(name, 1, 1, 554)
        assert r["errcode"] == 0
        assert r["id"] != None
        #查询部门
        print("&*&*&*&*&*&新增完成后开始查询部门**********")

        self.department.list("")
        assert self.department.jsonpath("$.department[?(@.id==%s)].id" % r["id"])[0] == 554
        assert self.department.jsonpath("$.department[?(@.id==%s)].name" % r["id"])[0] == name
        #更新部门
        if r["errcode"] == 0:
            upd_id = r["id"]
            update_r = self.department.update(upd_id, "修改后的测试部门"+str(datetime.now().second), 1, 1)
        assert update_r["errcode"] == 0
        print("&*&*&*&*&*&更新完成后开始查询部门**********")
        self.department.list("")
        assert self.department.jsonpath("$.department[?(@.id==%s)].id" % r["id"])[0] == 554
        assert self.department.jsonpath("$.department[?(@.id==%s)].name" % r["id"])[0] == "修改后的测试部门"+str(datetime.now().second)

        #删除部门
        del_r = self.department.delete(r["id"])
        assert del_r["errcode"] == 0


