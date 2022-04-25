# "添加数据"
import unittest
from unittest import suite
import requests
import os, sys
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from gevent import time

sys.path.append("D:\\Users\\15019\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages")


class Add(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/add"

    '''参数为空'''

    def test_add_params_null(self):
        r = requests.get(self.base_url, params={'name': ' ', 'age': ' '})
        self.result = r.json()
        self.assertEqual(self.result['code'], 10002)
        self.assertEqual(self.result['message'], '添加失败！')

    '''添加成功'''

    def test_add_success(self):
        r = requests.get(self.base_url, params={'name': '添加成功', 'age': 2022})
        self.result = r.json()
        self.assertEqual(self.result['code'], 200)
        self.assertEqual(self.result['message'], '添加成功！')

    def tearDown(self):
        pass


if __name__ == '__main__':
    # 指定端口和ip
    # unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Add)
    # 获取当前文件所在的路径
    base_dir = os.path.dirname(os.path.realpath(__file__))
    print(base_dir)
    dir_path = base_dir + "\\..\\report\\"
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    report_path = dir_path + now + "result.html"
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title="unittest报告", description="html测试:添加数据")
        runner.run(suite)
