from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random


def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4] #moss stone, cobblestone stairs, cobblestone
    block = random.choice(brokenBlocks) #choose one of the 3 possible blocks with 4 of them being the same
    return block

pos = mc.player.getTilePos() #retrieves the location of the player
x, y, z = pos.x, pos.y, pos.z

brokenWall = [] #creates an empty list called "brokenWall"
height, width = 5, 10 #assigns numbers to variables

# create the list of broken blocks
for row in range(height): #this should loop 5 tiems
    brokenWall.append([]) #puts a block in the list above
    for column in range(width): #this should loop 10 times
        block = brokenBlock() #grabs a random block of moss stone, cobblestone stairs or cobblestone
        brokenWall[row].append(block)

# set the blocks
for row in brokenWall: #this should loop 10 times.
    for block in row: 
        mc.setBlock(x, y, z, block) #put down a random block
        x += 1 #go to the next space 
    y += 1 #go up one block on the wall
    x = pos.x #start at the beginning of the wall
