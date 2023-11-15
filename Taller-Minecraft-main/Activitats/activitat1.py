# importem les llibreries i programes necessaris per fer que funcioni el programa
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connectar-se al servidor 
mc = minecraft.Minecraft.create()

#####################################################################
#                          ESCRIURE AL XAT                          #
#####################################################################

# escriurem al xat un missatge qualsevol
# ho farem amb .postToChat("missatge")

"""
    TO DO
"""


#####################################################################
#                        MOURE AL JUGADOR                           #
#####################################################################

# mourem el jugador a la posició x=-1, y=4, z=-1
# moure al jugador amb .player.setPos(x,y,z)

"""
    TO DO
"""

#####################################################################
#                          POSAR UN BLOC                            #
#####################################################################

# posarem un bloc qualsevol a la posició x=-2, y=4, z=-2
# ho farem amb .setBlock(x,y,z, tipus_bloc)

"""
    TO DO
"""


#####################################################################
#           COMPROVAR SI EL JUGADOR ESTÀ DAMUNT DEL BLOC            #
#####################################################################

# volem fer un codi que mentre el jugador NO estigui trepitjant un 
# bloc de TNT no es faci res, en el moment en què el jugador es
# posi damunt d'un TNT, volem que s'escrigui pel xat "SI! TNT"

"""
    PREGUNTA 1
"""

#####################################################################
#                        CONSTRUIR UNA CASA                         #
#####################################################################

# construïrem una casa de 7x6x7 (amplada, altura, llargària)
# ho farem amb .setBlocks(x1,y1,z1, x2,y2,z2, tipus_bloc)

"""
    TO DO
"""
