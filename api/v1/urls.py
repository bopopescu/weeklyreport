# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 9:52
# @Author  : jarvis7164
# @File    : urls.py
# @Software: PyCharm
# @Contact : 309194437@qq.com
from api.v1.views import *

api.add_resource(Hello, '/')
api.add_resource(Login, '/api/v1/login')
api.add_resource(Tasklist, '/api/v1/task')
api.add_resource(QueryTasklist, '/api/v1/query')
api.add_resource(UserList, '/api/v1/users')
api.add_resource(RoleList, '/api/v1/roles')
api.add_resource(DepartmentList, '/api/v1/departments')
api.add_resource(ProductList, '/api/v1/products')
api.add_resource(DictitemList, '/api/v1/dictitem')
api.add_resource(Dictitem_query, '/api/v1/dictitem/query')
api.add_resource(Weeklyreport_output, '/api/v1/weeklyreport_output')
api.add_resource(Weeklyreport_download, '/api/v1/weeklyreport_download')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
