
from api.wework import WeWork
from common.base_classes import BaseClasses


class Department(BaseClasses):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
    update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"

    def list(self, id):
        self.json_data = self.request_api('get', self.list_url, {"access_token": WeWork.get_access_token(), "id": id})
        print(self.verbose(self.json_data))
        return self.json_data

    def create(self, name, parentid, order, id):
        paramas = {"name": name, "parentid": parentid, "order": order, "id": id}
        self.json_data = self.request_api("post",self.create_url, params={"access_token": WeWork.get_access_token()},json=paramas)
        print(self.verbose(self.json_data))
        return self.json_data

    def delete(self, id):
        self.json_data = self.request_api("delete", self.delete_url, params={"access_token": WeWork.get_access_token(), "id": id})
        print(self.verbose(self.json_data))
        return self.json_data

    def update(self, id, name, parentid, order):
        paramas = {"id": id, "name": name, "parentid": parentid, "order": order}
        self.json_data = self.request_api("post",self.update_url, params={"access_token": WeWork.get_access_token()},json=paramas)
        print(self.verbose(self.json_data))
        return self.json_data

if __name__ == '__main__':
    print(Department().list(1))
    # print(Department().create("55pythonee",1,1,55))


