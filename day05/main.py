import logging

from utils.input import readinputfile2

def isWinner(board):
    rowhitcount=0
    for row in board:
        for cell in row:
            if cell == "X":
                rowhitcount+=1
        if rowhitcount == 5:
            return True
        rowhitcount=0

    colhitcount=0
    for y in range(len(board[0])):
        for x in range(len(board)):
            if board[x][y] == "X":
                colhitcount+=1
        if colhitcount == 5:
            return True
        colhitcount=0

    return False

def boardSum(board):

    sum=0
    for x in range(len(board)):
        for y in range(len(board[0])):
            #logging.debug(f"{board[x][y]}")
            if board[x][y] != 'X':
                sum = sum + int(board[x][y])

    logging.debug(f"Found Sum: {sum}")
    return sum

def puzzle01(data):
    #print(data)
    logging.debug("Executing Puzzle Stage 1")
    callednumbers = data[0].rstrip().split(",")

    boards = []
    for line in range(len(data)):
        #print(data[line])
        if line == 0:
            logging.debug("skipping 0 line.")
        elif data[line] == "" or data[line] == "\n":
            #logging.debug("new board detected")
            board = []
            boards.append(board)
        else:
            boards[len(boards)-1].append(data[line].rstrip().split(" "))
    #
    #print(callednumbers)
    for board in boards:
        for row in board:
            for item in row:
                if item == '':
                    row.remove('')
    #
    # for brd in boards:
    #     print("")
    #     for row in brd:
    #         print(row)

    for num in callednumbers:
        for brd in boards:
            for row in brd:
                for i in range(len(row)):
                    if row[i] == num:
                        row[i] = "X"
        # now after called number, check for any winners.
            if isWinner(brd):
                logging.debug(f"Board Winner Found: {num} on {brd}")
                finaloutput = (int(num) * int(boardSum(brd)))
                logging.debug(f"WinningNum: {finaloutput}")
                return finaloutput
        # if winner, return sum nonX #s * num
    #
    # logging.debug("Board Winner Not Found")
    # for brd in boards:
    #     print("")
    #     for row in brd:
    #         print(row)

    return 0

def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")
    callednumbers = data[0].rstrip().split(",")

    boards = []
    for line in range(len(data)):
        #print(data[line])
        if line == 0:
            logging.debug("skipping 0 line.")
        elif data[line] == "" or data[line] == "\n":
            #logging.debug("new board detected")
            board = []
            boards.append(board)
        else:
            boards[len(boards)-1].append(data[line].rstrip().split(" "))
    #
    #print(callednumbers)
    for board in boards:
        for row in board:
            for item in row:
                if item == '':
                    row.remove('')
    #
    # for brd in boards:
    #     print("")
    #     for row in brd:
    #         print(row)

    boardwinners=[False]*len(boards)
    #print(boardwinners)

    for num in callednumbers:
        for brdptr in range(len(boards)):

            for brdx in range(len(boards[brdptr])):
                for brdy in range(len(boards[brdptr][0])):

                    if boards[brdptr][brdx][brdy] == num:
                        boards[brdptr][brdx][brdy] = "X"

                    if isWinner(boards[brdptr]):
                        boardwinners[brdptr]=True
                        #if no winners, that board waas last winner
                        winctr = 0
                        for wins in boardwinners:
                            if wins == True:
                                winctr += 1
                        if winctr == len(boardwinners):
                            return int(num) * boardSum(boards[brdptr])

        # if winner, return sum nonX #s * num
    #
    # logging.debug("Board Winner Not Found")
    # for brd in boards:
    #     print("")
    #     for row in brd:
    #         print(row)

    return 0

def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    #Assuming Tests pass, run the final input
    runfinalinput()

