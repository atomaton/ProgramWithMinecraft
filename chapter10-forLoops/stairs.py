from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos() #function that obtains the postition of the player and puts that location in the variable 'pos"
x, y, z = pos.x, pos.y, pos.z #the position in the "pos" is then parsed out in to the 3 positions

stairBlock = 53 #this sets the variable "stairBlock" to the woodstair which is block ID 53

for step in range(10): #a for loop that creates 10 stairs as its run 10 times
    mc.setBlock(x + step, y + step, z, stairBlock) # x is over one and y is up one
