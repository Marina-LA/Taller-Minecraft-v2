import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connectar-se al servidor
mc = minecraft.Minecraft.create()

# moure al jugador a la posició 0 4 0 (x, y, z)
mc.player.setPos(0, 4, 0)

# funció que mira si el jugador està damunt d'un bloc de diamant 
# False -> si el bloc trepitjat no és de diamant
# True -> si el bloc trepitjat és de diamant
def bloc_trepitjat():
    player = mc.player.getTilePos()
    bloc = mc.getBlock(player.x, player.y-1, player.z)
    if bloc == block.DIAMOND_BLOCK.id:
        return True
    else:
        return False


# variable per controlar el bucle
bloc = bloc_trepitjat()



# exemple 1
"""
while True:
    mc.postToChat("Hola")
    time.sleep(3)
"""

# exemple 2

while bloc is False:
    mc.postToChat("No estem trepitjant diamant")
    time.sleep(3)
    bloc = bloc_trepitjat()

mc.postToChat("Estem damunt d'un bloc de diamant")

