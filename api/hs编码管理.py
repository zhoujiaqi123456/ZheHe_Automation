
def get_dict_hs(self):
    self.json_data = self.request('get_dict_hs.yaml')
    print(self.verbose(self.json_data))
    return self.json_data


def put_dict_hs(self):
    self.json_data = self.request('put_dict_hs.yaml')
    print(self.verbose(self.json_data))
    return self.json_data


