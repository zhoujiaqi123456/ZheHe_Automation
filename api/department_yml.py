
from api.wework import WeWork
from common.base_classes import BaseClasses


class DepartmentYml(BaseClasses):
    def list(self, id):
        self.json_data = self.request("api.yml", {"access_token": WeWork.get_access_token(), "id": id})
        print(self.verbose(self.json_data))
        return self.json_data
