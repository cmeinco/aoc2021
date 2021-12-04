
# util for handling the input, expected to read out of file
import logging

def readinputfile(filename):
    logging.debug(f"Reading {filename}")
    lines = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            lines.append(line)
    return lines

def readinputfile2(filename):
    logging.debug(f"Reading All Lines {filename}")
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    return lines
