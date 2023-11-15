import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connectar-se al servidor
mc = minecraft.Minecraft.create()

# moure al jugador a la posició 0 4 0 (x, y, z)
mc.player.setPos(0, 4, 0)

# funció que retorna el id del bloc trepitjat pel jugador
def bloc_trepitjat():
    player = mc.player.getTilePos()
    return mc.getBlock(player.x, player.y-1, player.z)



while True:
    # mirem quin bloc està trepitjant el jugador
    bloc = bloc_trepitjat()

    # exemple 1
    if bloc == block.DIAMOND_BLOCK.id:
        mc.postToChat("DIAMANT")
    elif bloc == block.GOLD_BLOCK.id:
        mc.postToChat("OR")
    elif bloc == block.LAPIS_LAZULI_BLOCK.id:
        mc.postToChat("LAPIS LAZULI")
    elif bloc == block.WOOL.id:
        mc.postToChat("LLANA")
    elif bloc == block.TNT.id:
        mc.postToChat("TNT")
    else:
        mc.postToChat(":(")


    time.sleep(1)