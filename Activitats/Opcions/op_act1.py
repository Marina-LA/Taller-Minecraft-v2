import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

#####################################################################
#                             PREGUNTA 1                            #
#####################################################################

#####
# A #
#####

player = mc.player.getTilePos()
bloc = mc.getBlock(player.x, player.y, player.z)

while bloc != block.TNT.id:
    player = mc.player.getTilePos()
    bloc = mc.getBlock(player.x, player.y, player.z)
    time.sleep(0.25)
mc.postToChat("SI! TNT")

#####
# B #
#####

player = mc.player.getTilePos()
bloc = mc.getBlock(player.x, player.y - 1, player.z)

for i in range(10):
    player = mc.player.getTilePos()
    bloc = mc.getBlock(player.x, player.y - 1, player.z)
    time.sleep(0.25)
mc.postToChat("SI! TNT")

#####
# C #
#####

player = mc.player.getTilePos()
bloc = mc.getBlock(player.x, player.y - 1, player.z)

while bloc != block.TNT.id:
    player = mc.player.getTilePos()
    bloc = mc.getBlock(player.x, player.y - 1, player.z)
    time.sleep(0.25)
mc.postToChat("SI! TNT")

#####
# D #
#####

player = mc.player.getTilePos()
bloc = mc.getBlock(player.x, player.y - 1, player.z)

while True:
    player = mc.player.getTilePos()
    bloc = mc.getBlock(player.x, player.y - 1, player.z)
    time.sleep(0.25)
mc.postToChat("SI! TNT")