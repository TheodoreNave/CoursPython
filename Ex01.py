#! /usr/bin/env python3
# coding: utf-8
import sys
import os

default_message = "Message I want to write in a files"

def read_file(file_name="default.txt"):

    fichier = open(file_name, 'r')
    file_content = fichiers.read()
    fichier.close

    return file_content

def write_file(message_to_write, file_name="default.txt"):

    fichier = open(file_name, "w+")
    fichier.write(message_to_write)
    fichier.close()


if __name__ == "__main__":

    print("Current Path:" + os.getcwd())

    print("Script name : ", sys.argv[0])
    print("Number of arguments : ", len(sys.argv))
    print("The arguemnts are : ", str(sys.argv))



    try:
            write_file(default_message, sys.argv[1])
            file_content = read_file(sys.argv[1])

    except IndexError:
            print("File Name not specified.")
            file_content = read_file()

    print("File Content : \n\n" + file_content)
