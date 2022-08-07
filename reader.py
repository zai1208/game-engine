import pygame
import sys


def split(file):
    temp_list = []
    temp_str = ""
    add_to_list = False

    num = 0
    num2 = 0
    len_line = 0
    linestr = []

    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        num += 1
        for char in line:
            num2 += 1
            if num2 == 1 and char == "[":
                add_to_str = True

        if add_to_str == True:
            if len(line) > 1:
                temp_str += line
                if line[1] == "/":
                    add_to_list = True
                    add_to_str = False

        if add_to_list == True:
            temp_list.append(temp_str)
            temp_str = ""
            add_to_list = False
        num2 = 0


    return temp_list

def parse(block):
    




if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(split(sys.argv[1]))
