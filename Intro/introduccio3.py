import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connectar-se al servidor
mc = minecraft.Minecraft.create()

# moure al jugador a la posició 0 4 0 (x, y, z)
mc.player.setPos(0, 4, 0)



# exemple 1
"""
for i in range(10):
    mc.postToChat(i)
"""

# exemple 2
"""
for i in range(2, 11, 2):
    mc.postToChat(i)
    time.sleep(1)
"""

# exemple 3

for i in range(10):
    mc.setBlock(2, 4+i, 2, block.CHEST.id)
    mc.postToChat(i)
    time.sleep(1)

