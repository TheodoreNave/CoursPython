#! /usr/bin/env python3
# coding: utf-8
import sys
import os

def my_WriteReadFunction():

    f = open("lol.txt", "w")
    f.write("Ligne1")
    f.close()
    f = open("lol.txt", "r")
    print(f.read())

    f = open("lol.txt", "w")
    os.rename("lol.txt", str(sys.argv[1]))
    f.write(str(sys.argv[2]))


def Read_function():

if __name__ == "__main__":
    my_WriteReadFunction()
    Read_function()
