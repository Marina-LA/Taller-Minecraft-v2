import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connectar-se al servidor
mc = minecraft.Minecraft.create()

# moure al jugador a la posició 0 4 0 (x, y, z)
mc.player.setPos(0, 4, 0)


# funció que retorna el id del bloc colpejat
def cop_bloc():
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        bloc = mc.getBlock(pos)
        if bloc == block.DIAMOND_BLOCK.id or bloc == block.GOLD_BLOCK.id:
            return mc.getBlock(pos)
        


while True:
    # mirem si hem colpejat el bloc corresponent
    bloc_colpejat = cop_bloc()

    # exemple 1
    """
    if bloc_colpejat == block.DIAMOND_BLOCK.id:
        mc.postToChat("DIAMANT!!")
    """


    # exemple 2
    """
    if bloc_colpejat == block.DIAMOND_BLOCK.id:
        mc.postToChat("DIAMANT!!")
    else:
        mc.postToChat(":(")
    """

    # exemple 3
    """
    if bloc_colpejat == block.DIAMOND_BLOCK.id or bloc_colpejat == block.GOLD_BLOCK.id:
        mc.postToChat("Bloc de DIAMANT o OR")
    """
        
    time.sleep(1)