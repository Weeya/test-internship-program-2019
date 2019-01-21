#!/usr/bin/env python
import xmltodict
import json
import sys

argument = sys.argv
inputFile = sys.argv[1]
def readFile():
    with open(inputFile) as File:
        doc = xmltodict.parse(File.read(), attr_prefix="")
        with open('weather.json','w') as jsonFile:
            json.dump(doc,jsonFile, indent=4)
        
def main():
    readFile()

main()
    