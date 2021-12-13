import logging

from utils.input import readinputfile2
import re
import sys

def incrementCell(x,y,dataset):
    flashes=0

    if x < 0 or x >= len(dataset): # out of bounds
        return 0
    if y < 0 or y >= len(dataset[0]): # out of bounds
        return 0
    #logging.debug(f"Incrementing: {x},{y}")
    if dataset[x][y] < 0:  # ignore if cell has already flashed
        return 0

    dataset[x][y] += 1
    if dataset[x][y] > 9:  # flash and set for reset to 0
        # flash
        flashes += 1
        dataset[x][y] = -10000  # maybe use for flash identifer?
        # add 1 to adjacents
        flashes += incrementCell(x + 1, y - 1, dataset)
        flashes += incrementCell(x + 1, y, dataset)
        flashes += incrementCell(x + 1, y + 1, dataset)
        flashes += incrementCell(x - 1, y - 1, dataset)
        flashes += incrementCell(x - 1, y, dataset)
        flashes += incrementCell(x - 1, y + 1, dataset)
        flashes += incrementCell(x,     y - 1, dataset)
        flashes += incrementCell(x,     y + 1, dataset)

    return flashes


def puzzle01(cycles, data):
    logging.debug("Executing Puzzle Stage 1")

    prevdataset = []

    for line in data:
        prevdataset.append(list(map(int, line.rstrip())))

    flashes=0
    cycleFlashes=0

    for i in range(0,cycles):

        logging.debug(f"Cycle {i}")

        for cell in range(0, len(prevdataset[0])):
            for row in range(0, len(prevdataset)):
                cycleFlashes+=incrementCell(row,cell,prevdataset)

        # # anything neg reset to 0
        # for row in prevdataset:
        #     for cell in row:
        #         print(f"{cell}\t",end="")
        #     print("")

        # anything neg reset to 0
        for row in range(0,len(prevdataset)):
            for cell in range(0,len(prevdataset[0])):
                if prevdataset[row][cell] < 0:
                    prevdataset[row][cell] = 0

        logging.debug(f"Cycle {i} flashed {cycleFlashes} / {flashes}")
        flashes += cycleFlashes
        cycleFlashes = 0


    return flashes


def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")

    cycles=1

    prevdataset = []

    for line in data:
        prevdataset.append(list(map(int, line.rstrip())))

    flashes=0
    cycleFlashes=0

    for i in range(0,1000):

        #logging.debug(f"Cycle {i}")

        for cell in range(0, len(prevdataset[0])):
            for row in range(0, len(prevdataset)):
                cycleFlashes+=incrementCell(row,cell,prevdataset)

        # # anything neg reset to 0
        # for row in prevdataset:
        #     for cell in row:
        #         print(f"{cell}\t",end="")
        #     print("")

        # anything neg reset to 0
        fla=0
        for row in range(0,len(prevdataset)):
            for cell in range(0,len(prevdataset[0])):
                if prevdataset[row][cell] < 0:
                    prevdataset[row][cell] = 0
                    fla+=1

        if fla==100:
            logging.debug(f"N Sync {cycles}")
            return cycles

        #logging.debug(f"Cycle {i} flashed {cycleFlashes} / {flashes}")
        flashes += cycleFlashes
        cycleFlashes = 0

        cycles+=1


    return 0


def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(100,finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # Assuming Tests pass, run the final input
    runfinalinput()
