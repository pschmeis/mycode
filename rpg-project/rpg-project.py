#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live
import os

def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
''')

# Returns a list of available directions from the current room.
def getLocations(room):
    options = []
    if 'up' in room:
        options.append('up')
    if 'down' in room: 
        options.append('down')
    if 'north' in room:
        options.append('north')
    if 'east' in room:
        options.append('east')
    if 'west' in room:
        options.append('west')
    if 'south' in room:
        options.append('south')
    return options
 
def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
    #get the available pathways
    locations = getLocations(rooms[currentRoom])
    print(f"You see exits to the: {locations}")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
            'Foyer' : {
                  'up'    : 'Stairway',
                  'north' : 'Kitchen',
                  'east'  : 'Sunroom',
                  'west'  : 'Lounge',
                },
            'Kitchen' : {
                  'east' : 'Dining Room',
                  'south' : 'Foyer',
                  'item'  : 'potion',
                },
            'Dining Room' : {
                  'west' : 'Kitchen',
                  'south': 'Sunroom',
                  'item' : 'knife',
               },
            'Sunroom' : {
                  'north' : 'Dining Room',
                  'west'  : 'Foyer',
               },
            'Lounge' : {
                  'north' : 'Office',
                  'east' : 'Foyer',
                  'item' : 'book',
               },
            'Office' : {
                  'south' : 'Lounge',
                  'item'  : 'whiskey',
               },
            'Stairway' : {
                  'down' : 'Foyer',
                  'north' : 'Master Bedroom',
                  'west' : 'Library',
                  'east' : 'Hallway',			  
               },
            'Library' : {
                  'west' : 'Balcony',
                  'east' : 'Stairway',
                  'item' : 'key',				  
               },
            'Master Bedroom' : {
                  'south' : 'Stairway',
                  'west' : 'Bathroom',
                  'monster' : 'idle',
                  'item' : 'foyer key',
                  'lock' : True,
               },
            'Hallway' : {
                  'north' : 'Craftroom',
                  'south' : 'Bedroom',
                  'west' : 'Stairway',
               },
            'Craftroom' : {
                  'south' : 'Hallway',		  
                  'item' : 'hammer',
               },
            'Bedroom' : {
                  'north' : 'Hallway',		  
               },
         }
       

#start the player in the Hall
currentRoom = 'Foyer'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
       move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    os.system('clear')

    #if they type 'go' first
    if move[0] == 'go' or move[0] == 'move':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            targetRoom = rooms[currentRoom][move[1]]
            if 'lock' in rooms[targetRoom] and rooms[targetRoom]['lock'] == True:
                print("That room is locked!")
            else:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' or move[0] == 'take' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    ## Item usage -- WIN CONDITIONS      
    if move[0] == 'use':
        if move[1] == 'hammer' and 'hammer' in inventory:
            if currentRoom == 'Library':
                print('You smash the window and excape!')
                break
            else:
                print("You don't see a way to use this here.")
        if move[1] == 'key' and 'key' in inventory:
            if currentRoom == 'Stairway':
                rooms['Master Bedroom']['lock'] = False
                inventory.remove('key')
                print("You unlock the master bedroom.")
            elif currentRoom == 'Foyer':
                print("The key does not fit this lock")

    ## Define how a player can win
    if currentRoom == 'Foyer' and 'foyer key' in inventory:
        print('You escaped the house safely... YOU WIN!')
        break

    ## If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    
