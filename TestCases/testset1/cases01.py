import unittest
import time


class Test01(unittest.TestCase):
    def setUp(self) -> None:
        print(f"{__file__} start to execute")

    def tearDown(self) -> None:
        time.sleep(2)
        print(f"{__file__} execution end")

    def test01(self):
        print("Execute the first case")

    def test02(self):
        print("Execute the second case")

    def test03(self):
        print("Execute the third case")


if __name__=="__main__":
    unittest.main()