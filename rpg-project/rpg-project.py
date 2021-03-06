#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live
import os

def showInstructions():
    #print a main menu and the commands
    print('''
You find yourself in a poorly lit house.
A sense of forboding fills the stagnant air.
The foyer door is locked behind you.
Find a way out before something... finds you.
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
    if 'description' in rooms[currentRoom]:
        print(rooms[currentRoom]['description'])
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
                  'description' : 'A dimly lit, drafty entrance to the residence.\nYou see stairs, doors on either side and what looks to be a kitchen just past the stairs.',
                },
            'Kitchen' : {
                  'east' : 'Dining Room',
                  'south' : 'Foyer',
                  'item'  : 'potion',
                  'description' : 'A sizable kitchen. You see an exit to the dining room and back to the foyer.',
                },
            'Dining Room' : {
                  'west' : 'Kitchen',
                  'south': 'Sunroom',
                  'item' : 'knife',
                  'description' : 'An impressive dining room with access to the kitchen and an easy transition to a sunroom.',
               },
            'Sunroom' : {
                  'north' : 'Dining Room',
                  'west'  : 'Foyer',
                  'description' : 'An odd sunroom. You see blackout drapes and what appears to be bars over the windows.',
               },
            'Lounge' : {
                  'north' : 'Office',
                  'east' : 'Foyer',
                  'item' : 'book',
                  'description' : 'If not for the... untoward smell wafting from the fireplace; this lounge would be quite cozy.',
               },
            'Office' : {
                  'south' : 'Lounge',
                  'item'  : 'whiskey',
                  'description' : 'So far, the only normal room in the house... which makes it odd?',
               },
            'Stairway' : {
                  'down' : 'Foyer',
                  'north' : 'Master Bedroom',
                  'west' : 'Library',
                  'east' : 'Hallway',
                  'description' : 'A sizable staircase with access to the second floor. A large door is on the north side.',
               },
            'Library' : {
                  'east' : 'Stairway',
                  'item' : 'key',
                  'description' : 'Large, but sturdy windows look to the outside. Perhaps there is some way to open them?',
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
                  'description' : 'A dark hallway with what looks like bedroom doors on either end.',
               },
            'Craftroom' : {
                  'south' : 'Hallway',		  
                  'item' : 'hammer',
                  'description' : 'Not a bedroom, but some sort of hobby room. But with a distinct lack of any projects underway.',
               },
            'Bedroom' : {
                  'north' : 'Hallway',
                  'description' : 'A sparsely furnished bedroom that would benefit from any color remotely brighter than \'dark grey.\'',
               },
         }
       

#start the player in the Hall
currentRoom = 'Foyer'

def main():
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
            if move[1] in inventory:
                if move[1] == 'hammer':
                    if currentRoom == 'Library':
                        print('You smash the window and excape!')
                        break
                    else:
                        print("You don't see a way to use this here.")
                elif move[1] == 'foyer key':
                    if currentRoom == 'Foyer':
                        print('You escaped the house safely... YOU WIN!')
                        break
                elif move[1] == 'key':
                    if currentRoom == 'Stairway':
                        rooms['Master Bedroom']['lock'] = False
                        inventory.remove('key')
                        print("You unlock the master bedroom.")
                    elif currentRoom == 'Foyer':
                        print("The key does not fit this lock")
                elif move[1] == 'whiskey': 
                    if 'monster' in rooms[currentRoom]:
                        rooms[currentRoom]['monster'] = 'pacified'
                        print("The shade accepts your offer.")
                        print("Instead of attacking you, the bottle becomes the victim.")
                    else:
                        print("You do not see a use for this here.")
            else:
                print(f"You do not have a {move[1]}.")

        ## If a player enters a room with a monster
        if 'monster' in rooms[currentRoom]:
            if rooms[currentRoom]['monster'] == 'idle':
                print('\u001b[31mThe room is unnaturally cold and you see a shadowy figure in the corner.\u001b[0m')
                rooms[currentRoom]['monster'] = 'awake'
            elif  rooms[currentRoom]['monster'] == 'awake':
                if 'knife' not in inventory and 'potion' not in inventory:
                    print('\u001b[31mThe cold shadow reacts to your presence and quickly engulfs you.')
                    print('Your vision goes black.')
                    break
                elif 'knife' in inventory:
                    print('\u001b[31mThe cold shadow reacts to your presence and moves toward you.')
                    print('As it reaches you, you strike out with your knife.')
                    print('After exchanging several blows you succumb to your wounds.')
                    break
                elif 'potion' in inventory:
                    print('\u001b[31mThe cold shadow reacts to your presence and moves toward you.')
                    print('Upon reaching you, it strikes out several times.')
                    print('Your potion is insufficient and you succumb to your wounds.')
                    break
                else:
                    rooms[currentRoom]['monster'] = 'dead'
                    print('\u001b[31mThe cold shadow reacts to your presence and moves toward you.')
                    print('After exchaning blows and utilizing your potion, the shade dissipates.')

if __name__ == '__main__':
    main()
