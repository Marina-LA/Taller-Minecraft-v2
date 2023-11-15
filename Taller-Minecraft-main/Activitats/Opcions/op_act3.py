import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
numero, x, y, z = 0
start = False
def getPlayerPos():
    pass



#####################################################################
#                             PREGUNTA 1                            #
#####################################################################

#####
# A #
#####

if numero == "0":
    bloc = block.AIR.id
elif numero == "1":
    bloc = block.BRICK_BLOCK.id
elif numero == "2":
    mc.setBlock(x, y-2, z, block.GOLD_BLOCK.id)
elif numero == "3":
    mc.setBlock(x, y-2, z, block.DIAMOND_BLOCK.id)
elif numero == "4":
    mc.setBlock(x, y-2, z, block.GLOWSTONE_BLOCK.id)


#####
# B #
#####

if numero == "1":
    bloc = block.AIR.id
elif numero == "1":
    bloc = block.BRICK_BLOCK.id
elif numero == "1":
    mc.setBlock(x, y-2, z, block.GOLD_BLOCK.id)
elif numero == "1":
    mc.setBlock(x, y-2, z, block.DIAMOND_BLOCK.id)
elif numero == "1":
    mc.setBlock(x, y-2, z, block.GLOWSTONE_BLOCK.id)


#####
# C #
#####

if numero == "0":
    bloc = block.AIR.id
elif numero == "1":
    bloc = block.BRICK_BLOCK.id
elif numero == "2":
    bloc = block.GOLD_BLOCK.id
elif numero == "3":
    bloc = block.DIAMOND_BLOCK.id
elif numero == "4":
    bloc = block.GLOWSTONE_BLOCK.id


#####################################################################
#                             PREGUNTA 2                            #
#####################################################################

#####
# A #
#####

def bloc_trepitjat():
    pos_jugador = getPlayerPos()
    return mc.getBlock(pos_jugador.x, pos_jugador.y-2, pos_jugador.z)


#####
# B #
#####

def bloc_trepitjat():
    pos_jugador = mc.player.getTilePos()
    return mc.getBlock(pos_jugador.x, pos_jugador.y-2, pos_jugador.z)

#####
# C #
#####

def bloc_trepitjat():
    pos_jugador = mc.player.getTilePos()
    bloc = mc.getBlock(pos_jugador.x, pos_jugador.y-2, pos_jugador.z)


#####################################################################
#                             PREGUNTA 3                            #
#####################################################################

#####
# A #
#####

while start:
    # obtenim el bloc trepitjat
    bloc = bloc_trepitjat()

    if bloc == block.GOLD_BLOCK.id:
        mc.postToChat("FRED")
    elif bloc == block.DIAMOND_BLOCK.id:
        mc.postToChat("CALENT")
    elif bloc == block.GLOWSTONE_BLOCK.id:
        mc.postToChat("HAS ARRIBAT AL FINAL!")
        start = False
    
    time.sleep(0.25)


#####
# B #
#####

while start:
    # obtenim el bloc trepitjat
    bloc = bloc_trepitjat()

    if bloc == block.GOLD_BLOCK.id:
        mc.postToChat("CALENT")
    elif bloc == block.DIAMOND_BLOCK.id:
        mc.postToChat("HAS ARRIBAT AL FINAL!")
    elif bloc == block.GLOWSTONE_BLOCK.id:
        mc.postToChat("FRED")
        start = False
    
    time.sleep(0.25)