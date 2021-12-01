import logging

def puzzle01(data):
    logging.debug(f"Executing Puzzle Stage 1")
    return "NotYetImplemented"

def puzzle02(data):
    logging.info(f"Executing Puzzle Stage 2")
    return "NotYetImplemented"

def readinputfile(filename):
    logging.debug(f"Reading {filename}")
    lines = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            lines.append(line)
    return lines

def runfinalinput():
    finaldata = readinputfile("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + puzzle01(finaldata))
    logging.info("Final Answer for Puzzle 2:" + puzzle02(finaldata))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #Assuming Tests pass, run the final input
    runfinalinput()

