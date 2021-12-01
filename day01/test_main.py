from unittest import TestCase
import logging

from day01.main import puzzle01

class Test(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

    def test_puzzle01(self):
        response = puzzle01("2,2,,2,2")
        expected = "2,2,,2,2"
        self.assertEqual(response,expected)
        logging.info("Answer for Puzzle 1:" + puzzle01("testthing1"))
        self.assertEqual(1, 1)

    def test_puzzle02(self):
        response = puzzle01("2,2,,2,2")
        expected = "2,2,,2,2"
        self.assertEqual(response,expected)
        logging.info("Answer for Puzzle 1:" + puzzle02("testthing1"))
        self.assertEqual(1, 1)
