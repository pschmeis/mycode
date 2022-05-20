#!/usr/bin/env python3

from classpowers import classinfo

def main():

    for student in classinfo.get('all'):
        print(f"{student.get('name')}, an {student.get('skill level')} {student.get('spirit animal')} of a programmer, possesses a {student.get('super power')} factor for moonlighting as a superher!")

main()
