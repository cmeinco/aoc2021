import logging

from utils.input import readinputfile

def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")
    nums = []
    for item in data:
        nums.append(int(item))

    count=0
    for x in range(0, len(nums)):
        if x == 0:
            continue
        else:
            if nums[x] > nums[x-1]:
                count += 1

    return count

def puzzle02(data):
    originnums = []
    for item in data:
        originnums.append(int(item))

    nums = []
    for x in range(0, len(originnums)-2):
        nums.append(originnums[x]+originnums[x+1]+originnums[x+2])

    count=0
    for x in range(0, len(nums)):
        if x == 0:
            continue
        else:
            if nums[x] > nums[x-1]:
                count += 1

    return count

def runfinalinput():
    finaldata = readinputfile("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #Assuming Tests pass, run the final input
    runfinalinput()

