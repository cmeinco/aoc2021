import logging

from utils.input import readinputfile

def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")

    depth=0
    horiz=0

    for line in data:
        item=int(line.split()[1])
        if line.__contains__("down"):
            depth=depth+item
        elif line.__contains__("up"):
            depth=depth-item
        elif line.__contains__("forward"):
            horiz=horiz+item

    return horiz*depth

def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")

    depth=0
    horiz=0
    aim=0

    for line in data:
        item=int(line.split()[1])
        if line.__contains__("down"):
            #depth=depth+item
            aim=aim-item
        elif line.__contains__("up"):
            #depth=depth-item
            aim=aim+item
        elif line.__contains__("forward"):
            horiz=horiz+item
            depth=depth+(aim*item)

    return abs(horiz*depth)


def runfinalinput():
    finaldata = readinputfile("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #Assuming Tests pass, run the final input
    runfinalinput()

