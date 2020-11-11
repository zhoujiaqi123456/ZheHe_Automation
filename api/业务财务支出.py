
def post_outcome_check(self):
    self.json_data = self.request('post_outcome_check.yaml')
    print(self.verbose(self.json_data))
    return self.json_data


def put_outcome_check(self):
    self.json_data = self.request('put_outcome_check.yaml')
    print(self.verbose(self.json_data))
    return self.json_data


def post_outcome_check_fee(self):
    self.json_data = self.request('post_outcome_check_fee.yaml')
    print(self.verbose(self.json_data))
    return self.json_data


def post_outcome_check_refuse(self):
    self.json_data = self.request('post_outcome_check_refuse.yaml')
    print(self.verbose(self.json_data))
    return self.json_data


def post_outcome_check_todo(self):
    self.json_data = self.request('post_outcome_check_todo.yaml')
    print(self.verbose(self.json_data))
    return self.json_data


