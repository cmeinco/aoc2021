from unittest import TestCase
import logging

from day01.main import puzzle01
from day01.main import puzzle02
from utils.input import readinputfile


class Test(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_puzzle01(self):
        input = readinputfile("test_file_1.txt")
        expected = 7
        response = puzzle01(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 1:" + str(response))

    def test_puzzle02(self):
        input = readinputfile("test_file_1.txt")
        expected = 5
        response = puzzle02(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 2:" + str(response))
