#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    lat = resp['iss_position']['latitude']
    lon = resp['iss_position']['longitude']
    coords = (lat, lon)

    result = rg.search(coords)

    print("\nCurrent Location of the ISS")
    print(f"Timestamp: {datetime.datetime.fromtimestamp(resp['timestamp'])}")
    print(f"Lat: {lat}")
    print(f"Lon: {lon}")
    print(f"{result[0]['name']}, {result[0]['cc']}")

if __name__ == "__main__":
    main()
