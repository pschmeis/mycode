#!/usr/bin/env python3

## create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

## display parts of the dictionary
print( switch["hostname"] )
print( switch["ip"] )

## request a 'fake' key
# print( switch["lynx"] )   # Be sure to comment out this line,
                            # or your program will CONTINUE to fail!
                            # if a KEY is requested that does not exist,
                            # an ERROR will be thrown!

## request a 'fake' key with .get() method
print( "\nFirst test - .get()" )
print( switch.get("lynx") )

print( "\nSecond test - .get()" )
print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

print( "\nThird test - .get()" )
print( switch.get("version") )

print( "\nFourth test - .keys()" )
print( switch.keys() )

print( "\nFifth test - .values()" )
print( switch.values() )

print( "\nSixth test - .pop()" )
switch.pop("version") # removes this key (and value) pair
print( switch.keys() )   # notice the value of version is gone
print( switch.values() ) # notice the value 1.2

print( "\nSeventh test - ADD a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values() )

print( "\nEighth test - ADD a new value" )
switch["password"] = "qwerty"
print( switch.keys() )
print( switch.values() )

