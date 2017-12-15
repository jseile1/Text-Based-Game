from __future__ import print_function
import random

playerItems = []
enteredRooms = []
openedDoors = []

def startGame():
    print('Welcome to the mysterious mansion')
    raw_input('Press enter to start the game. ')
    room1()

def room1():
    global playerItems
    global enteredRooms
    global openedDoors
    exitRoom = False
    dresserItems = ['key1', 'flashlight']
    print('You have entered the foyer')
    print('There are two doors in this room.  One to the left(door 1) and one to the right(door2).')
    print('There is also a dresser with one drawer in the room.')
    userAction = raw_input('What would you like to do? ')
    while exitRoom == False:
        if userAction == 'open door 1' and 'key1' in playerItems:
            print('The door slowly creaks open')
            openedDoors += ['door1']
            exitRoom = True
        elif userAction == 'open door 2' and 'flashlight' in playerItems:
            print('You open the door and can now see inside with the flashlight.')
            openedDoors += ['door2']
            exitRoom = True
        elif userAction == 'open dresser':
            print('You picked up', dresserItems)
            playerItems += dresserItems
            dresserItems = []
            userAction = raw_input('What would you like to do now? ')
        elif userAction == 'open door 1' and 'key1' not in playerItems:
            print('The door will not open')
            userAction = raw_input('What would you like to do now? ')
        elif userAction == 'open door 2' and 'flashlight' not in playerItems:
            print('You open the door, but it is so dark inside that you cannot see.  You do not enter and you close the door.')
            userAction = raw_input('What would you like to do now? ')
        else:
            userAction = raw_input('Not a valid action.  Try Again! ')
    if 'door1' in openedDoors:
        room2()
    else:
        room3()
        
def room2():
    global enteredRooms
    print('You entered Room 2')
    if 'room2' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'room2' not in enteredRooms:
        enteredRooms += ['room2']
        
def room3():
    global enteredRooms
    print('You entered Room 3')
    if 'room3' in enteredRooms:
        print('This room looks vaguely familiar')
    if 'room3' not in enteredRooms:
            enteredRooms += ['room3']