from datetime import datetime
from api.department import Department
from common.data_base import DataBase
import pytest
import time


class TestDepartment:
    # 先实例化对象
    department = Department()
    db = DataBase(department.get_config("MYSQL", "HOST"), department.get_config("MYSQL", "PORT"),
                  department.get_config("MYSQL", "USER"), department.get_config("MYSQL", "PASSWORD"),
                  department.get_config("MYSQL", "DATABASE"))

    def setup_class(self):
        pass

    @pytest.mark.usefixtures("del_user")
    # 标记使用指定fixture(测试准备及清理方法)
    def test_list(self):
        r = self.department.list("1")
        #断言
        assert r["errcode"] == 0
        assert r["department"][0]["name"] == "墨迹测试"
        #和数据库对比
        sql2 = 'SELECT * FROM student where age=20'
        d = [{'id': 1, 'nickName': '小小', 'shortName': '大大', 'age': 20},
             {'id': 2, 'nickName': '小红', 'shortName': '大红', 'age': 20}]
        c = self.db.check_result(d, sql2)
        print(c)

    def test_create(self):
        name = "测试部门" + str(datetime.now().second)

        r = self.department.create(name, 1, 1, 434)
        assert r["errcode"] == 0
        assert r["id"] != None

        # 写法一：
        # exist = False
        # for depart in self.department.list("")["department"]:
        #     if depart["id"] == r["id"]:
        #         exist = True
        # assert exist == True

        #写法二：
        self.department.list("")
        print("&*&*&*&*&*&")
        print(self.department.jsonpath("$.department[?(@.id==%s)].id" % 1)[0])
        print(self.department.jsonpath("$.department[?(@.id==%s)].name" % 1)[0])

        assert self.department.jsonpath("$.department[?(@.id==%s)].id" % r["id"])[0] == 434
        assert self.department.jsonpath("$.department[?(@.id==%s)].name" % r["id"])[0] == name


    def test_delete(self):
        cre_r = self.department.create("测试部门5", 1, 1, 250)
        if cre_r["errcode"] == 0:
            del_id = cre_r["id"]
            time.sleep(5)
            del_r = self.department.delete(del_id)
        assert del_r["errcode"] == 0

    def test_update(self):
        cre_r = self.department.create("测试部门777", 1, 1, 270)
        if cre_r["errcode"] == 0:
            upd_id = cre_r["id"]
            update_r = self.department.update(upd_id, "修改后的测试部门777", 1, 1)
        assert update_r["errcode"] == 0

    # def test_update(self):
    #     depart = self.department.list("")['department'][1]
    #     id = depart['id']
    #     name = depart['name']
    #     assert self.department.update(id, name=name + '1')['errcode'] == 0
    #     assert self.department.list(id)['department'][0]['name'] == name + '1'



