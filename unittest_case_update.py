import os
import sys
import unittest
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner
from gevent import time
from test_case.test_update import Update

sys.path.append("D:\\Users\\15019\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages")


if __name__ == '__main__':
    # 指定端口和ip
    # unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Update)
    suite = unittest.TestSuite([suite1])

    # 获取当前文件所在的路径
    base_dir = os.path.dirname(os.path.realpath(__file__))
    print(base_dir)
    dir_path = base_dir + "\\..\\201901020216_陈彬彬_1\\report\\"
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    report_path = dir_path + now + "result.html"
    with open(report_path,'wb')as f:
        runner = HTMLTestRunner(stream=f,verbosity=2,title="unittest报告",description="html测试:修改数据")
        runner.run(suite)