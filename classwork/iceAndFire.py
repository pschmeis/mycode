#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"
AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF)
    gotresp2 = requests.get(AOIF_BOOKS)

    ## Decode the response
    got_dj = gotresp.json()
    got_dj2 = gotresp2.json()

    ## print the response
    print(got_dj)
    print(got_dj2)

if __name__ == "__main__":
    main()

