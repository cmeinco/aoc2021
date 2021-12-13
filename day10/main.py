import logging

from utils.input import readinputfile2
import re
import sys

def parseString(ptr, inputdata, tokens):

    stack = []

    for i in range(ptr, len(inputdata)):
        # if opening, consume and parse further
        # if 4 deep can only be closed by last opened.
        if inputdata[i] in ["[","{","(","<"]:
            stack.append(inputdata[i])
        else:
            popper = stack.pop()
            if popper != tokens[inputdata[i]]["inverse"]:
                # inverse of popper was expected
                expectedchar="unknown"
                if popper == "{":
                    expectedchar="}"
                elif popper == "[":
                    expectedchar="]"
                elif popper == "(":
                    expectedchar=")"
                elif popper == "<":
                    expectedchar=">"
                tokens[inputdata[i]]["count"]+=1
                logging.debug(f"exception; {expectedchar}; popper={popper}; inputdata[i]={inputdata[i]}; stack={stack}")
                raise AOCException(f"Expected {expectedchar}")



# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
class AOCException(Exception):
    pass


def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")
    tokens = {}
    tokens["("] = {"count": 0, "points": 3, "inverse": ")"}
    tokens["["] = {"count": 0, "points": 57, "inverse": "]"}
    tokens["{"] = {"count": 0, "points": 1197, "inverse": "}"}
    tokens["<"] = {"count": 0, "points": 25137, "inverse": ">"}
    tokens[")"] = {"count": 0, "points": 3, "inverse": "("}
    tokens["]"] = {"count": 0, "points": 57, "inverse": "["}
    tokens["}"] = {"count": 0, "points": 1197, "inverse": "{"}
    tokens[">"] = {"count": 0, "points": 25137, "inverse": "<"}

    for line in data:

        inputval = list(line.rstrip())
        logging.debug(f"{inputval}")
        try:
            something = parseString(0, inputval, tokens)
        except AOCException as e:
            #msg = str(e)
            logging.debug(f"Exception yo: {e}")
            # increment count of bad chars

    logging.debug(f"tokens={tokens}")
    syntaxscore = 0
    for item in ["]","}",")",">"]:
        syntaxscore += (tokens[item]["count"]*tokens[item]["points"])

    return syntaxscore


def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")


    return 0


def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # Assuming Tests pass, run the final input
    runfinalinput()
