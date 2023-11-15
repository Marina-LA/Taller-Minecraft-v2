# importem les llibreries i programes necessaris per fer que funcioni el programa
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connectar-se al servidor 
mc = minecraft.Minecraft.create()

# nom del fitxer que conté el laberint
FITXER = "laberint.txt"

# obrim el fitxer del laberint per llegir-lo
file = open(FITXER, "r")

# moure al jugador a la posició x=-1, y=altura_jugador, z=-1
pos_jugador = mc.player.getTilePos()
mc.player.setPos(-1, pos_jugador.y, -1)

# posar un bloc de lapis lazuli a prop del jugador
mc.setBlock(-5, pos_jugador.y, -5, block.LAPIS_LAZULI_BLOCK.id)

#####################################################################
#                     CONSTRUCCIÓ DEL LABERINT                      #
#####################################################################

POS_X = 0
POS_Y = pos_jugador.y
POS_Z = 0

z = POS_Z

for line in file.readlines():
    # agafar els números de la línia
    # eliminem el salt de línia i separem els números 
    linia = line.rstrip()
    dades = linia.split(":")

    # posició inicial on començarem a construir el laberint
    x = POS_X

    y = POS_Y

    # bucle per tractar els números d'una línia un per un
    for numero in dades:

        bloc = block.AIR.id
        # volem posar el condicional que controla per quin bloc estem passant
        # depenent del valor de la variable "numero"
        # haureu de posar un bloc o un altre en una variable anomenada "bloc"
        # ex:   bloc = block.TIPUS.id
        # numero = 0 -> bloc d'aire (AIR)
        # numero = 1 -> bloc de maó (BRICK_BLOCK)
        # numero = 2, 3, 4 -> bloc d'aire (AIR)
        # en els números 2, 3, 4 haureu de posar un bloc d'un tipus corresponent dues
        # posicions per sota del jugador. Els tipus són els següents:
        # numero = 2 -> posar un bloc d'or (GOLD_BLOCK)
        # numero = 3 -> posar un bloc de diamant (DIAMOND_BLOCK)
        # numero = 4 -> posar un bloc de glowstone (GLOWSTONE_BLOCK)
        """
            PREGUNTA 1
        """



        # comencem a construir el laberint
        # li posem 5 blocs d'altura
        mc.setBlock(x, POS_Y, z, bloc)
        mc.setBlock(x, POS_Y+1, z, bloc)
        mc.setBlock(x, POS_Y+2, z, bloc)
        mc.setBlock(x, POS_Y+3, z, bloc)
        mc.setBlock(x, POS_Y+4, z, bloc)
    
        # construïm el terra del laberint, hi posem un bloc de pedra
        mc.setBlock(x, POS_Y-1, z, block.STONE_BRICK.id)

        bloc = block.AIR.id

        # ens movem a la següent coordenada x dins de la línia
        # cada coordenada x representa posar un bloc en la paret de laberint
        x += 1      # equival a posar x = x + 1
    
    # ens movem a la següent coordenada z per posar la següent fila del laberint
    # cada coordenada z representa posar una fila de paret nova en el laberint
    z += 1      # equival a posar z = z + 1




#####################################################################
#                      FUNCIÓ BLOC TREPITJAT                        #
#####################################################################

# volem retornar el bloc que està trepitjant el jugador
# hem de tenir en compte que heu d'obtenir la posició del jugador
# en el moment en què es crida a aquesta funció
# heu de mirar dues posicions per sota del jugador (pos.y-2)

    """
        PREGUNTA 2
    """




#####################################################################
#                      CONTROL DEL LABERINT                         #
#####################################################################

# creem una variable booleana que ens ajudarà a saber si el joc ha començat o no
# si False --> joc no començat 
# si True --> joc començat
start = False

while not start:
    events = mc.events.pollBlockHits()
    for e in events:
        posicio = e.pos
        if posicio.x == POS_X-5 and posicio.y == POS_Y and posicio.z == POS_Z-5:
            start = True
            mc.postToChat("COMENCEM EL JOC!") 
            mc.postToChat("TROBA EL FINAL DEL LABERINT!")
    time.sleep(0.5)




# BUCLE DE CONTROL DEL JOC
# mentre la variable start sigui true s'ha d'executar el bucle
# heu d'utilitzar la funció creada anteriorment per veure quin bloc s'ha trepitjat
# depenent del tipus de bloc haureu de posar un missatge pel xat o un altre
# bloc = GOLD -> posar un missatge avisant que aquest no és el camí correcte
# bloc = DIAMOND -> posar un missatge avisant que aquest és el camí correcte
# bloc = GLOWSTONE -> posar un missatge avisant que s'ha arribat al final del laberint
# a més a més, en trepitjar el bloc de GLOWSTONE haureu de posar la variable start a False
# poseu un time.sleep(0.25) al final del bucle
"""
    PREGUNTA 3
"""


# movem al jugador a l'inici del laberint
mc.player.setPos(POS_X-1, POS_Y, POS_Z-1)