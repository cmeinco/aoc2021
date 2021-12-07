import logging

from utils.input import readinputfile2
import re

hitmap = {}


def calcFishCount(day, fishstate) -> {}:
    # always short circuit in case we have the data/recursion
    fishkey=f"day{day}-state{fishstate}"
    if not hitmap.get(fishkey):
        # calc and add to map
        if day == 0:
            logging.debug(f"Hit 0day: {fishstate}")
            hitmap[fishkey] = {"fishcount": 1}
            return hitmap.get(fishkey)
        else:
            fishcount = 0
            if fishstate == 0:
                fishcount += calcFishCount(day - 1, 8)["fishcount"] # new fish
                fishcount += calcFishCount(day - 1, 6)["fishcount"] # old fish
            else:
                fishcount += calcFishCount(day - 1, fishstate - 1)["fishcount"]
            hitmap[fishkey] = {"fishcount": fishcount}

    return hitmap.get(fishkey)


def getFishCount(day, fishstate):
    count = calcFishCount(day, fishstate).get("fishcount")
    #logging.debug(f"Final hitmap: {hitmap}")
    return count

def puzzle01(days, data):
    logging.debug("Executing Puzzle Stage 1")

    initdata = list(map(int, data[0].split(",")))
    logging.debug(f"Days: {days}, {initdata}")

    # if in hitmap return value else calculate value
    fishcount = 0
    for fishy in initdata:
        fishcount += getFishCount(days, fishy)
        #logging.debug(f"Fishcount after {days} days on initial state {fishy}: {fishcount}")
    #logging.debug(f"Fishcount after {days} days on initial state {initdata[0]}: {fishcount}")

    return fishcount


def puzzle02(day, data):
    logging.debug("Executing Puzzle Stage 2")

    return puzzle01(day, data)


def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(80, finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(256, finaldata)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Assuming Tests pass, run the final input
    runfinalinput()
