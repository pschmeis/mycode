#!/usr/bin/env python3

def main():    
    usr_name = input("Please enter your name:\n>") 
              
    usr_name = usr_name.title()    
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
            
    zodiac = {
            '7' : ['Rabbit', 'vigilant', 'witty', 'quick-minded','ingenious'],
            '4' : ['Rat', 'artistic', 'sociable', 'industrious', 'charming', 'intelligent'],
            '6' : ['Tiger', 'courageous', 'enthusiastic', 'confident', 'charismatic', 'a leader'],
            '5' : ['Ox', 'strong', 'thorough', 'determined', 'loyal', 'reliable'], 
            '8' : ['Dragon', 'talented', 'powerful', 'lucky', 'successfull'],
            '9' : ['Snake', 'wise', 'like to work alone','determined'],
            '10': ['Horse', 'animated', 'active', 'energetic'],
            '11': ['Sheep', 'creative', 'resilient', 'gentle', 'mild-mannered', 'shy'],
            '0' : ['Monkey', 'sharp', 'smart', 'curious', 'mischievious'],
            '1' : ['Rooster', 'hardworking', 'resourceful', 'courageous', 'talented'],
            '2' : ['Dog', 'loyal', 'honest', 'cautious', 'kind'],
            '3' : ['Pig', 'a symbol of wealth', 'honesty', 'practicality'],
            }

    lookup = usr_date % 12
    print(f"{user_name} your zodiac sign is {zodiac[lookup][0]")
    if usr_date in [2011, 1999, 1987, 1975, 1963]:
    elif usr_date in [2020, 2008, 1996, 1984, 1972, 1960]:
    elif usr_date in [2010, 1998, 1986, 1974, 1962]:
    elif usr_date in [2021, 2009, 1997, 1985, 1973, 1961]:
    elif usr_date in [2012, 2000, 1988, 1976, 1964]:    
    elif usr_date in [2013, 2001, 1989, 1977, 1965]:
    elif usr_date in [2014, 2002, 1990, 1978, 1966]:
    elif usr_date in [2015, 2003, 1991, 1979, 1967]:
    elif usr_date in [2016, 2004, 1992, 1980, 1968]:
    elif usr_date in [2017, 2005, 1993, 1981, 1969]:
    elif usr_date in [2018, 2006, 1994, 1982, 1970]:
    elif usr_date in [2019, 2007, 1995, 1983, 1971]:


main()
