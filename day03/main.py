import logging

from utils.input import readinputfile


def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")

    linect=0
    onebit=0
    zerbit=0

    cols = range(len(data[0]))
    finaloutput1 = []
    finaloutput2 = []

    for col in cols:
        #print(f"{col}")
        #print(f"COL{col}")
        for line in data:

            #print(f"LINE: {line}")

            if line[col] == "1":
                onebit += 1
            else:
                zerbit += 1

        if zerbit > onebit:
            finaloutput1.append("0") # gamma
            finaloutput2.append("1") # epsilon
        else:
            finaloutput1.append("1") # gamme
            finaloutput2.append("0") # epsilon
        zerbit=0
        onebit=0
        linect=0

    logging.debug(f"finaloutput1/gamma - {finaloutput1}")
    logging.debug(f"finaloutput2/epsil - {finaloutput2}")

    gamma = int("".join(finaloutput1), 2)
    espil = int("".join(finaloutput2), 2)

    return gamma*espil

def getMostCommon(datalist):
    mostcommon=None
    countone=0
    countzer=0
    for item in datalist:
        if item == "1":
            countone+=1
        else:
            countzer+=1
    if countone >= countzer:
        return "1"
    else:
        return "0"



def get_oxygen_generator_rating(data,pos=0):
    # most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
    # If 0 and 1 are equally common, keep values with a 1 in the position being considered.

    if len(data) == 1:
        return data[0]

    subdataset=[]
    cols = range(len(data[0]))
    onebit=0
    zerbit=0
    for line in data:
        if line[pos] == "1":
            onebit += 1
        else:
            zerbit += 1

    if zerbit > onebit: # filter to 0s at pos
        for line in data:
            if line[pos] == "0":
                subdataset.append(line)

    else: # filter to 1s at pos
        for line in data:
            if line[pos] == "1":
                subdataset.append(line)

    return get_oxygen_generator_rating(subdataset, pos+1)

def get_CO2_scrubber_rating(data,pos=0):
    # least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position.
    # If 0 and 1 are equally common, keep values with a 0 in the position being considered.

    if len(data) == 1:
        return data[0]

    subdataset=[]
    cols = range(len(data[0]))
    onebit=0
    zerbit=0
    for line in data:
        if line[pos] == "1":
            onebit += 1
        else:
            zerbit += 1

    if zerbit > onebit: # filter to 0s at pos
        for line in data:
            if line[pos] == "1":
                subdataset.append(line)

    else: # filter to 1s at pos
        for line in data:
            if line[pos] == "0":
                subdataset.append(line)

    return get_CO2_scrubber_rating(subdataset, pos+1)


def get_life_support_rating(data):
    return int(get_oxygen_generator_rating(data),2) * int(get_CO2_scrubber_rating(data),2)

def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")

    return get_life_support_rating(data)

def runfinalinput():
    finaldata = readinputfile("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #Assuming Tests pass, run the final input
    runfinalinput()

