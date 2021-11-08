import unittest
import os
import time

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

case_path = os.path.join(os.getcwd(), 'testset1')
# case_path = os.getcwd()

# def get_test_dirs(path):
#     dirs = []
#     for dir in os.listdir(path):
#         if os.path.isdir(dir) and 'testset' in dir:
#             dirs.append(dir)
#     return dirs
#
#
# def get_dir_cases(dir):
#     discover = unittest.defaultTestLoader.discover(dir, pattern='cases*.py')
#     return discover


def all_cases():
    discover = unittest.defaultTestLoader.discover(case_path, pattern='cases*.py', top_level_dir=None)
    return discover


if __name__ == "__main__":
    report_dir = os.path.join(os.getcwd(), 'reports')
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)
    report_path = os.path.join(report_dir, time.strftime("%Y_%m_%d_%h_%m_%s") + "_result.html")
    with open(report_path, 'w+') as f:
        runner = HTMLTestRunner(stream=f, title="Test Report Portal", description="Test Report")
        runner.run(all_cases())
    print("************Test Finished!**************")
