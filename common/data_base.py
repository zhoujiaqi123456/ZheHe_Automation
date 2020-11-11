#!/usr/local/bin/python3

# -*- coding: UTF-8 -*-
import pymysql


class DataBase:
	def __init__(self, host, port, user, password, database):
			# 建立连接通道，建立连接填入（连接数据库的IP地址，端口号，用户名，密码，要操作的数据库，字符编码）
			self.conn = pymysql.connect(
				host=host,
				port=int(port),  # 注意这里得把port转换成int！
				user=user,
				password=password,
				database=database,
				charset="utf8"
			)

			# 创建游标，操作设置为字典类型，返回结果为字典格式！不写默认是元组格式！
			self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

	def query(self, sql_string):
		r = self.cursor.execute(sql_string)
		req = self.cursor.fetchall()  # 接收返回的所有数据
		query_data = {'total': r, 'data': req}
		self.conn.commit()  # 提交
		# 操作完成之后，就需要关闭连接
		self.cursor.close()  # 关闭游标
		self.conn.close()  # 关闭连接
		return query_data

	def compare_dict(self, response, result):
		# 判断字典response的key的值是否与result字典key的值相一致
		is_equal = True
		for key in result.keys():
			if response[self.hump_to_underline(key)] != result[key]:
				is_equal = False
				break
		return is_equal

	def compare_dict_raise(self, response, result):
		# 判断字典response的key的值是否与result字典key的值相一致
		is_equal = True
		for key in result.keys():
			if response[self.hump_to_underline(key)] != result[key]:
				raise Exception("接口返回和数据库字段值不一致!", key, response[self.hump_to_underline(key)], result[key])
				is_equal = False
				break
		return is_equal

	def ergodic_list(self, response, result):
		# 判断字典response是否与result列表中的某个字典相匹配
		is_equal = False
		for item in result:
			if self.compare_dict(response, item):
				is_equal = True
				print('返回结果{0} 与 数据库中的 {1} 一致'.format(response, item))
				# break
		return is_equal

	def ergodic_list_raise(self, response, result):
		# 判断字典response是否与result列表中的某个字典相匹配
		is_equal = False
		for item in result:
			if self.compare_dict_raise(response, item):
				is_equal = True
				print('返回结果{0} 与 数据库中的 {1} 一致'.format(response, item))
				# break
		return is_equal

	def ergodic_dict(self, response, result):
		# 判断两个列表中存放的字典中的key值是否一致
		is_equal = True
		for item in response:
			if not self.ergodic_list(item, result):
				is_equal = False
				print('返回结果{0} 与 数据库数据不一致'.format(item))
				# break
		return is_equal

	def check_list_result(self,response, result):
		if not self.ergodic_list(response, result):
			raise Exception('返回结果与数据库不一致')

	def check_result(self, response, sql_string):
		"""
		接口返回的response格式要求[{},{},{}]
		:param response：接口返回值
		:param sql_string：sql语句
		"""
		print('****************sql****************语句为：', sql_string)
		result = self.query(sql_string)
		s = "数据库返回结果"
		print(s.center(50, '*'), result['data'])
		if not self.ergodic_dict(response, result['data']):
			print("接口返回总数为: {0} ;".format(len(response)), "数据库返回总数为: {0} ".format(result['total']))
			raise Exception('对比失败，接口返回和数据库不一致')
		else:
			print(True)

	def check_single_result(self, response, sql_string):
		"""
		接口返回的response格式要求{}
		:param response：接口返回值
		:param sql_string：sql语句
		"""
		print('****************sql****************语句为：', sql_string)
		result = self.query(sql_string)
		s = "数据库返回结果"
		print(s.center(50, '*'), result['data'])
		if not self.ergodic_list_raise(response, result['data']):
			raise Exception('Fail-compare,response and result ')
		else:
			print(True)

	def hump_to_underline(self, text):
		arr = filter(None, text.lower().split('_'))
		res = ''
		for i in arr:
			res = res + i[0].upper() + i[1:]
		return res[0].lower() + res[1:]

	@classmethod
	def check_total(cls,sql,total):
		result = cls.query(sql)
		assert int(total) == result['total'], '返回结果{0} 与 数据库数据{1}不一致'.format(int(total),result["total"])

	@classmethod
	def check_dict_results(cls, response, sql):
		result = cls.query(sql)
		for key in response.keys():
			assert response[key] == result[key]


#删除字典中值为null的 并返回字典
def traversingDict(json):
    for key in list(json.keys()):
        if isinstance(json[key], dict):
            print(key + "是字典，需要继续遍历")
            traversingDict(json[key])
        elif isinstance(json[key], list):
            for i in json[key]:
                traversingDict(i)
        elif json[key] is None:
            print(key + "为None")
            del json[key]
        elif not json[key]:
            del json[key]
    return json


if __name__ == '__main__':
	sql = 'SELECT * FROM student where age=10'

	sql2 = 'SELECT * FROM student where age=20'
	d = [{'id': 1, 'nickName': '小小', 'shortName': '大大', 'age': 20}, {'id': 2, 'nickName': '小红', 'shortName': '大红', 'age': 20}]
	# c = DataBase("47.98.255.48",8008,"zhehe_qa","zhehe_qa_123B","zhehe_qa").check_result(d,sql2)
	# c=DataBase(get_config("MYSQL","HOST"),get_config("MYSQL","PORT"),get_config("MYSQL","USER"),get_config("MYSQL","PASSWORD"),get_config("MYSQL","DATABASE")).check_result(d,sql2)
	e = {'id': 3, 'nickName': '小白', 'shortName': '大白人', 'age': 10}
	c = DataBase("47.98.255.48",8008,"zhehe_qa","zhehe_qa_123B","zhehe_qa").query(sql)
	print(c)
	we = DataBase("47.98.255.48",8008,"zhehe_qa","zhehe_qa_123B","zhehe_qa").check_single_result(e,sql)
	print(we)


# a= DataBase("47.98.255.48",8008,"zhehe_qa","zhehe_qa_123B","zhehe_qa").query(sql)
	# a= DataBase("47.98.255.48",8008,"zhehe_qa","zhehe_qa_123B","zhehe_qa").query(sql)

	# a = DataBase(Config().get_config('MYSQL', 'HOST'), Config().get_config('MYSQL', 'PORT'),
	# 					  Config().get_config('MYSQL', 'USER'), Config().get_config('MYSQL', 'PASSWORD'),
	# 					  Config().get_config('MYSQL', 'DATABASE')).query(sql)
	# b=[{'id': 1, 'name': '小明', 'age': 24, 'adress': '浙江杭州余杭区'}, {'id': 3, 'name': '小张', 'age': 20, 'adress': '浙江杭州江干区'}]






