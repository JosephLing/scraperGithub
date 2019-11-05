import os
import csv

def check(content):
    lines = content.readlines()
    for line in lines:
        # need to use csv lib for this
        if len(line.split(",")):
            pass

def main():
    for file in os:
        with open(file, 'r', encoding='utf8') as fileData:
            check(fileData)

if __name__ == "__main__":
    main()