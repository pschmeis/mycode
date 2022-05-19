#!/usr/bin/python3

import datetime



def main():
    signs = [{'name': 'Aquarius', 'classic': '01-20', 'new': '02-16'},
            {'name': 'Pisces', 'classic': '02-19', 'new': '03-11'},
            {'name': 'Aries', 'classic': '03-21', 'new': '04-18'},
            {'name': 'Taurus', 'classic': '04-20', 'new': '05-13'},
            {'name': 'Gemini', 'classic': '05-21', 'new': '06-21'},
            {'name': 'Cancer', 'classic': '06-21', 'new': '07-20'},
            {'name': 'Leo', 'classic': '07-23', 'new': '08-10'},
            {'name': 'Virgo', 'classic': '08-23', 'new': '09-16'},
            {'name': 'Libra', 'classic': '09-23', 'new': '10-30'},
            {'name': 'Scorpio', 'classic': '10-23', 'new': '11-23'},
            {'name': 'Ophiuchus', 'classic': '13-00', 'new': '11-29'},
            {'name': 'Sagittarius', 'classic': '11-22', 'new': '12-17'},
            {'name': 'Capricorn', 'classic': '12-22', 'new': '01-20'}]

    print('\nThe constellations have shifted in the sky since zodiac originated.')
    print('In 2016 NASA released corrected dates for Zodiac signs.')
    print("To find out your 'real' sign:")

    again = True

    while again:
        # Set continue to false because python is silly and doesnt have do-until loops
        again = False

        month = input("\nEnter your month [01-12]: ")
        day = input("And day of birth [01-31]: ")
        
        combo = month + "-" + day

        # Iterate through dictionary to find zodiacs
        for sign in signs:
            
            if combo < "01-20":
                old = "Capricorn"
            elif combo >= sign.get('classic'):
                old = sign.get('name')
            
            if combo < "02-16":
                modern = "Capricorn"
            elif combo >= sign.get('new') and sign.get('name') != "Capricorn" :
                modern = sign.get('name')
        
        print(f'\nYour standard zodiac is {old} and your modern (real) zodiac is {modern}\n')

        response = input('Would you like to check another date? (Y/N): ')
        if response.lower() == 'y':
            again = True

main()












