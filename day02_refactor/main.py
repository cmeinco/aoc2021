import logging

from utils.input import readinputfile
import re

def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")

    depth=0
    horiz=0

    for line in data:
        m = re.match(r"^(?P<action>[a-z]+) +(?P<amt>\d+)$", line)
        if m:
            if m.group("action") == "down":
                depth = depth+int(m.group("amt"))
            elif m.group("action") == "up":
                depth = depth-int(m.group("amt"))
            elif m.group("action") == "forward":
                horiz = horiz+int(m.group("amt"))

    return horiz*depth


def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")

    depth = 0
    horiz = 0
    aim = 0

    for line in data:
        m = re.match(r"^(?P<action>[a-z]+) +(?P<amt>\d+)$", line)
        if m:
            if m.group("action") == "down":
                aim += int(m.group("amt"))
            elif m.group("action") == "up":
                aim -= int(m.group("amt"))
            elif m.group("action") == "forward":
                horiz += int(m.group("amt"))
                depth += (aim * int(m.group("amt")))

    return horiz*depth



def runfinalinput():
    finaldata = readinputfile("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #Assuming Tests pass, run the final input
    runfinalinput()

