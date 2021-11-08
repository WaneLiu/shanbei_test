import unittest
import ddt


@ddt.ddt
class test_ddt(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @ddt.data(2, 3)
    def test_01(self, data):
        print(data)

    @ddt.file_data('data.json')
    def test_02(self, data):
        print(data)

    @ddt.file_data('yaml.yml')
    def test_03(self, name, age, sex):
        print(name, age, sex)
