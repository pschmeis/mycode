#!/usr/bin/python3
"""opening a static file containing JSON data | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## open the file
    with open("classdata.json", "r") as data:
        datadecoded = json.load(data)

    ## This is now a dictionary
    print(type(datadecoded))

    ## display the servers in the datacenter
    #print(datadecoded)

    ## display the servers in row3
    #print(datadecoded["row3"])

    ## display the 2nd server in row2
    #print(datadecoded["row2"][1])

if __name__ == "__main__":
    main()

