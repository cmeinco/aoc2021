from unittest import TestCase
import logging

from day02_refactor.main import puzzle01
from day02_refactor.main import puzzle02
from utils.input import readinputfile


class Test(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_puzzle01(self):
        input = readinputfile("test_file_1.txt")
        expected = 150
        response = puzzle01(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 1:" + str(response))

    def test_puzzle01_final(self):
        input = readinputfile("finalinput.txt")
        expected = 1635930
        response = puzzle01(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 1:" + str(response))

    def test_puzzle02(self):
        input = readinputfile("test_file_1.txt")
        expected = 900
        response = puzzle02(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 2:" + str(response))

    def test_puzzle02_final(self):
        input = readinputfile("finalinput.txt")
        expected = 1781819478
        response = puzzle02(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 2:" + str(response))
