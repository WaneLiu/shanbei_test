import unittest
from selenium import webdriver


class UnitBase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
