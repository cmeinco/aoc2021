from unittest import TestCase
import logging

from day10.main import puzzle01
from day10.main import puzzle02
from utils.input import readinputfile2


class Test(TestCase):
    def setUp(self) -> None:
        logging.basicConfig(level=logging.DEBUG)

# Legal: ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).
# Corrupt:
#     {([(< {}[<>[]} > {[]{[( < () > - Expected], but found }  instead.
#     [[<[([])) < ([[{}[[()]]] - Expected], but found ) instead.
#     [{[{({}]{}}([{[{{{}}([] - Expected), but found ] instead.
#     [ < (< ( < ( < {})) > < ([]([]() - Expected >, but found ) instead.
#     < {([([[(<> ()){}] > (<< {{- Expected ], but found > instead.
# Incomplete:

    def test_puzzle01(self):
        input = readinputfile2("test_file_1.txt")
        expected = 26397
        response = puzzle01(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 1:" + str(response))

    def test_puzzle02(self):
        input = readinputfile2("test_file_1.txt")
        expected = 1134
        response = puzzle02(input)
        self.assertEqual(expected, response)
        logging.info("Testing Answer for Puzzle 2:" + str(response))
