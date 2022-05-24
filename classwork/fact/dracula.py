#!/usr/bin/env python3


   
with open("dracula.txt", "r") as dracula:
    count = 0
    for line in dracula:
        if "vampire" in line.lower():
            count += 1
            with open("vampytimes.txt", "a") as vamps:
                vamps.write(line + "\n")

    print(count)
