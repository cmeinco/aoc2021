from unittest import TestCase
import logging

from day08.main import puzzle01
from day08.main import puzzle02
from utils.input import readinputfile2


class Test(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_puzzle01(self):
        input = readinputfile2("test_file_1.txt")
        expected = 26
        response = puzzle01(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 1:" + str(response))

    def test_puzzle02(self):
        input = readinputfile2("test_file_1.txt")
        expected = 61229
        response = puzzle02(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 2:" + str(response))
