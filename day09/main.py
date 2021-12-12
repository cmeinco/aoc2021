import logging

from utils.input import readinputfile2
import re
import sys

board = []


def isLowest(x, y, board):
    # logging.debug(f"Checking {x},{y}")
    x_min = 0
    y_min = 0
    x_max = len(board) - 1
    y_max = len(board[0]) - 1

    friends = 0
    lowerFriends = 0

    if (x != x_min):  # check x-1
        # logging.debug(f"down: {x} {x_min}")

        if (board[x - 1][y] <= board[x][y]):
            lowerFriends += 1
        friends += 1

    if (y != y_min):  # check y-1
        # logging.debug(f"left: {y} {y_min}")

        if (board[x][y - 1] <= board[x][y]):
            lowerFriends += 1
        friends += 1

    if (x != x_max):  # check x+1
        # logging.debug(f"up: {x} {x_max}")

        if (board[x + 1][y] <= board[x][y]):
            lowerFriends += 1
        friends += 1

    if (y != y_max):  # check y+1
        # logging.debug(f"right: {y} {y_max}")
        # logging.debug(f"right: {y} {y_max}")
        if (board[x][y + 1] <= board[x][y]):
            lowerFriends += 1
        friends += 1

    # logging.debug(f"lowerfriends: {lowerFriends}")
    return (lowerFriends == 0)


def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")
    risk = 0
    for line in data:
        board.append(list(map(int, line.rstrip())))

    logging.debug(f"Board: {board}")

    lowest_x = []
    lowest_y = []

    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if isLowest(x, y, board):
                lowest_x.append(x)
                lowest_y.append(y)

    logging.debug(f"xs: {lowest_x}")
    logging.debug(f"ys: {lowest_y}")
    logging.debug(f"count: {len(lowest_y)}")

    for x in range(0, len(lowest_x)):
        risk += (board[lowest_x[x]][lowest_y[x]] + 1)

    return risk
    # 1880 too high
    # 550 wasn't checking if =


def getBasinSize(board, x, y, prevnum, firstrun=False):
    # find the 9s and edges then stop
    size = 1
    if y < 0 or y >= len(board[0]):
        return 0
    if x < 0 or x >= len(board):
        return 0
    if board[x][y] == 9:
        return 0
    if board[x][y] == -1:
        return 0
    logging.debug(f"{x},{y}: Boardxy: {board[x][y]} ? prevnum {prevnum}; first: {firstrun}")
    if board[x][y] <= prevnum and not firstrun:
        logging.debug(f"xy<prevnum; return 0")
        return 0

    prevnum = board[x][y]
    board[x][y] = -1
    # check neighbors who havent been checked.
    # check up
    size += getBasinSize(board, x + 1, y,     prevnum)
    # check down
    size += getBasinSize(board, x - 1, y,     prevnum)
    # check right
    size += getBasinSize(board, x,     y + 1, prevnum)
    # check left
    size += getBasinSize(board, x,     y - 1, prevnum)
    return size


def getBasinSize_broken(board, x, y, prevnum, firstrun=False):
    # find the 9s and edges then stop
    size = 1
    if y < 0 or y >= len(board[0]):
        return 0
    if x < 0 or x >= len(board):
        return 0
    if board[x][y] == 9:
        return 0
    if board[x][y] == -1:
        return 0
    if board[x][y] > prevnum and not firstrun:
        return 0
    else:
        prevnum=board[x][y]
        board[x][y] = -1
        # check neighbors who havent been checked.
        # check up
        size += getBasinSize(board, x + 1, y, prevnum)
        # check down
        size += getBasinSize(board, x - 1, y, prevnum)
        # check right
        size += getBasinSize(board, x, y + 1, prevnum)
        # check left
        size += getBasinSize(board, x, y - 1, prevnum)
    return size



def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")

    for line in data:
        board.append(list(map(int, line.rstrip())))

    logging.debug(f"Board: {board}")

    lowest_x = []
    lowest_y = []

    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if isLowest(x, y, board):
                lowest_x.append(x)
                lowest_y.append(y)
    #
    # logging.debug(f"xs: {lowest_x}")
    # logging.debug(f"ys: {lowest_y}")
    logging.debug(f"count: {len(lowest_y)}")

    # now have the lowest points
    # find the basin size of each point

    logging.debug("-----PRE ANALYSIS------")
    for x in range(len(board)):
        logging.debug(f"{board[x]}")


    basinSizes = []

    for x in range(0, len(lowest_x)):
        # basically search for edges or 9s and stop
        #evalmap = board.copy()
        basinSizes.append(
            getBasinSize(board, lowest_x[x], lowest_y[x],
                         board[lowest_x[x]][lowest_y[x]], firstrun=True)
        )
        # logging.debug("-----MAP-----")
        # for x in range(len(evalmap)):
        #     logging.debug(f"{evalmap[x]}")
        #logging.debug(evalmap)

    logging.debug("-----POST ANALYSIS------")
    for x in range(len(board)):
        logging.debug(f"{board[x]}")

    basinSizes.sort()
    basinSizes.reverse()
    logging.debug(f"BasinSizes: {basinSizes}")
    count1s=0
    count9s=0
    totalcells=0
    for x in board:
        for cell in x:
            if cell == -1:
                count1s += 1
            elif cell == 9:
                count9s +=1
            else:
                logging.debug(f"Found strange {cell} in {x}")
            totalcells+=1
    logging.debug(f"sumbasin: {sum(basinSizes)}; -1s: {count1s}; 9s: {count9s}; 9s1ssum:{count9s+count1s} total: {totalcells}; ")

    return basinSizes[0] * basinSizes[1] * basinSizes[2]
    # 6887120 too high
    # 3323784 too high
    # 1211862 too high

def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Assuming Tests pass, run the final input
    runfinalinput()
