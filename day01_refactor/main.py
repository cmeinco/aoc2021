import logging

from utils.input import readinputfile2

def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")
    count = 0
    for x in range(1, len(data)):
        if int(data[x]) > int(data[x-1]):
            count += 1
    return count

def puzzle02(data):
    nextdata=[]
    for x in range(0, len(data)-2):
        nextdata.append(int(data[x])+int(data[x+1])+int(data[x+2]))
    return puzzle01(nextdata)

def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #Assuming Tests pass, run the final input
    runfinalinput()

