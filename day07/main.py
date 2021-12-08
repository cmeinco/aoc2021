import logging

from utils.input import readinputfile2
import re
import sys

def getMinFuelUsed(data):

    max_num = max(data)

    minfuel=sys.maxsize

    for num in data:
        f = getFuelUsed(num,data)
        if f<minfuel:
            minfuel=f

    return minfuel

def getFuelUsed(dst, data):
    fuel = 0
    for crab in data:
        fuel+=abs(crab-dst)
    return fuel

def getSuperFuelUsed(dst, data):
    fuel = 0
    #for x in range(min(data), max(data)+1):
    for crab in data:
        steps = abs(crab-dst)
        if steps>0:
            for x in range(1, steps+1):
                fuel += x
    return fuel

def getMinFuelUsed2(data):

    max_num = max(data)

    minfuel=sys.maxsize

    #for num in data:
    logging.debug(f"min {min(data)} max {max(data)}")
    for num in range(min(data), max(data)+1):
        f = getSuperFuelUsed(num, data)
        if f<minfuel:
            minfuel=f
            logging.debug(f"Found new min: {minfuel}") # used to cheat cause didn't know how long it would run for. wasnt too long.

    return minfuel

def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")
    initdata = list(map(int, data[0].split(",")))
    logging.debug(f"{initdata}")
    #average_of_nums = sum(initdata) / len(initdata)

    minfuel = getMinFuelUsed(initdata)

    return minfuel


def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")
    initdata = list(map(int, data[0].split(",")))
    logging.debug(f"{initdata}")
    # average_of_nums = sum(initdata) / len(initdata)

    minfuel = getMinFuelUsed2(initdata)

    return minfuel


def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Assuming Tests pass, run the final input
    runfinalinput()
