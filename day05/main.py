import logging

from utils.input import readinputfile2
import re


def puzzle01(data):
    logging.debug("Executing Puzzle Stage 1")

    srcxs = []
    srcys = []
    dstxs = []
    dstys = []

    for line in data:
        m = re.match("^(\d+), *(\d+) *-> *(\d+), *(\d+)$", line)
        if m:
            srcxs.append(int(m.group(1)))
            srcys.append(int(m.group(2)))
            dstxs.append(int(m.group(3)))
            dstys.append(int(m.group(4)))

        # whichever is equal, draw line between other two.

    # logging.debug(srcxs)

    coveredpoints = {}

    for i in range(len(srcxs)):
        if srcxs[i] == dstxs[i]:
            # x is same / vert line
            # logging.debug(f"x same;vert line {srcxs[i]},{srcys[i]}->{dstxs[i]},{dstys[i]}")
            for y in range(min(srcys[i], dstys[i]), max(srcys[i], dstys[i]) + 1):
                key = f"{srcxs[i]}-{y}"
                # logging.debug(f"Updating {key}")
                if not coveredpoints.get(key):
                    coveredpoints[key] = 0
                coveredpoints[key] = int(coveredpoints[key]) + 1
            # logging.debug(f"Board\n{coveredpoints}")

        elif srcys[i] == dstys[i]:
            # y is same / horiz line
            # logging.debug(f"y same;horzn line {srcxs[i]},{srcys[i]}->{dstxs[i]},{dstys[i]}")

            for x in range(min(srcxs[i], dstxs[i]), max(srcxs[i], dstxs[i]) + 1):
                key = f"{x}-{srcys[i]}"
                # logging.debug(f"Updating {key}")
                if not coveredpoints.get(key):
                    coveredpoints[key] = 0
                coveredpoints[key] = int(coveredpoints[key]) + 1
            # logging.debug(f"Board\n{coveredpoints}")

        else:
            # logging.debug(f"Line Not Hzn/Vrt, Skipping. {srcxs[i]},{srcys[i]}->{dstxs[i]},{dstys[i]}")
            pass
    #
    # for x in range(0,10):
    #     for y in range(0,10):
    #         val=coveredpoints.get(f"{x}-{y}")
    #         if val:
    #             print(val,end="")
    #         else:
    #             print(".",end="")
    #     print()

    # logging.debug(f"Final Board {coveredpoints}")
    count = 0
    for k, v in coveredpoints.items():
        if v > 1:
            count += 1
    return count


def puzzle02(data):
    logging.debug("Executing Puzzle Stage 2")

    srcxs = []
    srcys = []
    dstxs = []
    dstys = []

    for line in data:
        m = re.match("^(\d+), *(\d+) *-> *(\d+), *(\d+)$", line)
        if m:
            srcxs.append(int(m.group(1)))
            srcys.append(int(m.group(2)))
            dstxs.append(int(m.group(3)))
            dstys.append(int(m.group(4)))

        # whichever is equal, draw line between other two.

    # logging.debug(srcxs)

    coveredpoints = {}

    for i in range(len(srcxs)):
        if srcxs[i] == dstxs[i]:
            # x is same / vert line
            # logging.debug(f"x same;vert line {srcxs[i]},{srcys[i]}->{dstxs[i]},{dstys[i]}")
            for y in range(min(srcys[i], dstys[i]), max(srcys[i], dstys[i]) + 1):
                key = f"{srcxs[i]}-{y}"
                # logging.debug(f"Updating {key}")
                if not coveredpoints.get(key):
                    coveredpoints[key] = 0
                coveredpoints[key] = int(coveredpoints[key]) + 1
            # logging.debug(f"Board\n{coveredpoints}")

        elif srcys[i] == dstys[i]:
            # y is same / horiz line
            # logging.debug(f"y same;horzn line {srcxs[i]},{srcys[i]}->{dstxs[i]},{dstys[i]}")

            for x in range(min(srcxs[i], dstxs[i]), max(srcxs[i], dstxs[i]) + 1):
                key = f"{x}-{srcys[i]}"
                # logging.debug(f"Updating {key}")
                if not coveredpoints.get(key):
                    coveredpoints[key] = 0
                coveredpoints[key] = int(coveredpoints[key]) + 1
            # logging.debug(f"Board\n{coveredpoints}")

        else:
            #logging.debug(f"Line Slanted. {srcxs[i]},{srcys[i]}->{dstxs[i]},{dstys[i]}")
            sx = 0
            sy = 0
            dx = 0
            dy = 0
            if srcxs[i] > dstxs[i]:
                # rev flow
                sx = dstxs[i]
                sy = dstys[i]
                dx = srcxs[i]
                dy = srcys[i]
            else:
                # normal
                sx = srcxs[i]
                sy = srcys[i]
                dx = dstxs[i]
                dy = dstys[i]
            slopeup = True
            if sy > dy:
                slopeup = False
            #logging.debug(f"SlopeUp?{slopeup}:{sx},{sy}->{dx},{dy}")
            x = sx
            y = sy
            while x <= dx:
                key = f"{x}-{y}"
                #logging.debug(f"Updating {key}")
                if not coveredpoints.get(key):
                    coveredpoints[key] = 0
                coveredpoints[key] = int(coveredpoints[key]) + 1

                x += 1
                if slopeup:
                    y += 1
                else:
                    y -= 1

    #
    # for x in range(0, 10):
    #     for y in range(0, 10):
    #         val = coveredpoints.get(f"{x}-{y}")
    #         if val:
    #             print(val, end="")
    #         else:
    #             print(".", end="")
    #     print()

    # logging.debug(f"Final Board {coveredpoints}")
    count = 0
    for k, v in coveredpoints.items():
        if v > 1:
            count += 1
    return count

    return 0


def runfinalinput():
    finaldata = readinputfile2("finalinput.txt")
    logging.info("Final Answer for Puzzle 1:" + str(puzzle01(finaldata)))
    logging.info("Final Answer for Puzzle 2:" + str(puzzle02(finaldata)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Assuming Tests pass, run the final input
    runfinalinput()
