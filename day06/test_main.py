from unittest import TestCase
import logging

from day06.main import puzzle01
from day06.main import puzzle02
from utils.input import readinputfile2


class Test(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_puzzle01(self):
        input = readinputfile2("test_file_1.txt")
        expected = 26  # 18 loops; 5934 # 80 loops
        response = puzzle01(18, input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 1:" + str(response))

    def test_puzzle01_80(self):
        input = readinputfile2("test_file_1.txt")
        expected = 5934  # 80 loops
        response = puzzle01(80, input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 1:" + str(response))

    def test_puzzle02(self):
        input = readinputfile2("test_file_1.txt")
        expected = 26984457539
        response = puzzle02(256, input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 2:" + str(response))
