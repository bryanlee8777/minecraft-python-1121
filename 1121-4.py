from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

count = 0

while count<5:
    mc.setBlocks(x+10,y-1,z,x-10,y-10,z,19)
    z = z + 2
    count = count + 1    
