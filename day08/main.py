import logging

from utils.input import readinputfile2
import re
import sys

#
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")
    digits = 0
    for item in data:
        initdata = item.rstrip().split("|")[1].split(" ")
        logging.debug(f"initial data {initdata}")
        for elem in initdata:
            # #s 1,4,7,8
            if len(elem) == 2 or \
                    len(elem) == 4 or \
                    len(elem) == 3 or \
                    len(elem) == 7:
                digits+=1
            logging.debug(f"{elem} {len(elem)}; {digits}")

    return digits
#
# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315

def compareBlocks(left,right):
    # return how many left blocks are in right
    count = 0
    for l in list(left):
        if l in list(right):
            count+=1
    return count

def decodeOutput(outputdata,finalcodes):
    value = []
    for item in outputdata:
        logging.debug(f"checking {item}")
        for numkey,val in finalcodes.items():
            if len(item) == len(val["inputcodes"]) and \
                    compareBlocks(val["inputcodes"], item) == len(item):
                value.append(numkey)
                logging.debug(f"found {item} == {numkey}")
                break
    return int(''.join(value))

def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")
    finalvalue = 0
    for item in data:
        inputdata = item.rstrip().split("|")[0].split(" ")
        inputdata.remove('')
        outputdata = item.rstrip().split("|")[1].split(" ")
        outputdata.remove('')
        logging.debug(f"initial data {inputdata} ||| {len(inputdata)} ||| {outputdata}")

        finalcodes={}
        #map 1,4,7,8
        #    2,4,3,7
        loopcount=0
        quickfinds=True
        while(len(finalcodes.keys())!=10 and loopcount<100000):
            if quickfinds:
                for elem in inputdata:
                    # get 1
                    if len(elem) == 2:
                        finalcodes["1"] = {"inputcodes": elem}
                    if len(elem) == 4:
                        finalcodes["4"] = {"inputcodes": elem}
                    if len(elem) == 3:
                        finalcodes["7"] = {"inputcodes": elem}
                    if len(elem) == 7:
                        finalcodes["8"] = {"inputcodes": elem}
                quickfinds=False
                #logging.debug(f"map={finalcodes}")

            # figure out the rest.
            # options: a,b,c,d,e,f,g

            # 1 - done
            # 4 - done
            # 7 - done
            # 8 - done
            # 6 - 6 blocks; only 1 of 1
            # 0 - 6 blocks; both 1, only 3 of 4
            # 9 - 6 blocks; both 1, all of 4
            # 3 - 5 blocks; both 1
            # 2 - 5 blocks; only 1 of 1, all but 2 of 6
            # 5 - 5 blocks; only 1 of 1, all but 1 of 6

            for elem in inputdata:

                if len(elem) == 6:
                    if compareBlocks(finalcodes["1"]["inputcodes"], elem) == 2:
                        if compareBlocks(finalcodes["4"]["inputcodes"], elem) == 3:
                            if not finalcodes.get("0"):
                                finalcodes["0"] = {"inputcodes": elem}
                        elif compareBlocks(finalcodes["4"]["inputcodes"], elem) == 4:
                            if not finalcodes.get("9"):
                                finalcodes["9"] = {"inputcodes": elem}
                    elif compareBlocks(finalcodes["1"]["inputcodes"], elem) == 1:
                        if not finalcodes.get("6"):
                            finalcodes["6"] = {"inputcodes": elem}

                if len(elem) == 5:
                    if compareBlocks(finalcodes["1"]["inputcodes"], elem) == 2:
                        if not finalcodes.get("3"):
                            finalcodes["3"] = {"inputcodes": elem}
                    elif compareBlocks(finalcodes["1"]["inputcodes"], elem) == 1:
                        if finalcodes.get("6"): # 6 needs to be completed first.
                            if compareBlocks(finalcodes["6"]["inputcodes"], elem) == 4:
                                if not finalcodes.get("2"):
                                    finalcodes["2"] = {"inputcodes": elem}
                            elif compareBlocks(finalcodes["6"]["inputcodes"], elem) == 5:
                                if not finalcodes.get("5"):
                                    finalcodes["5"] = {"inputcodes": elem}

            loopcount+=1
            if loopcount==5000:
                logging.debug("Taking a long time...")

        logging.debug(f"codemap={finalcodes}")
        # now we have the input codes decoded
        logging.debug(f"{outputdata}")
        value = decodeOutput(outputdata,finalcodes)
        logging.debug(f"{outputdata}: {value}")
        finalvalue += value

    return finalvalue


def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Assuming Tests pass, run the final input
    runfinalinput()
