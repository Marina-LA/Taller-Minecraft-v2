# importem les llibreries i programes necessaris per fer que funcioni el programa
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# connectar-se al servidor 
mc = minecraft.Minecraft.create()

#####################################################################
#                          EVENTS DE BLOC                           #
#####################################################################
# volem tenir una funció que ens retorni el bloc al que se li ha
# donat un cop

"""
    PREGUNTA 1
"""

#####################################################################
#                          EVENTS DE XAT                            #
#####################################################################
# volem tenir una funció que ens retorni el missatge que s'ha 
# escrit pel xat

"""
    PREGUNTA 2
"""

#####################################################################
#                          QUIÉN ES QUIÉN                           #
#####################################################################
# programarem el joc de "Quién es quién" per poder jugar amb la màquina

# llista de blocs amb els quals jugarem
blocs =[block.ICE.id, block.WOOL.id, block.GOLD_ORE.id, \
        block.WOOD.id, block.DIRT.id, block.LEAVES.id, block.TNT.id, \
        block.BOOKSHELF.id, block.DIAMOND_ORE.id, block.MELON.id]

# llista de pistes per cada bloc
pista_bloc = {0:["blau"], \
              1:["blanc"], \
              2:["groc"], \
              3:["marro"], \
              4:["marro"], \
              5:["verd"], \
              6:["vermell", "blanc"], \
              7:["blau", "marro", "verd", "groc", "vermell", "blanc"], \
              8:["blau"], \
              9:["verd"]}

# fem que la màquina triï un bloc aleatòriament
bloc_maquina = random.randint(0, 9)

# col·loquem els blocs en el món
for i in range(10):
    pos_jugador = mc.player.getTilePos()
    mc.setBlock(pos_jugador.x+i, pos_jugador.y, pos_jugador.z, blocs[i])


#####################################################################
#                         FUNCIÓ COMPROVACIÓ                        #
#####################################################################

# funció que comprovarà si el bloc que ha triat la màquina compleix amb el que hem dit
def comprovacio(missatge):
    # s'agafen les pistes per al bloc que ha triat la màquina
    llista_pistes = pista_bloc[bloc_maquina]

    # si el jugador no ha introduït cap missatge, no es fa la comprovació
    if missatge == None:
        return None
    
    # volem tenir un bucle que miri per cada pista que es trobi en la 
    # llista llista_pistes si aquesta pista és igual al missatge que
    # hi ha en la variable missatge
    # SI és igual -> posem pel xat "<maquina> SI"
    # NO és igual -> posem pel xat "<maquina> NO"

    """
        PREGUNTA 3
    """
    


# variable que controlarà el joc
start = True
mc.postToChat("Comencem el joc!")

# bucle principal del joc
while start:

    # volem fer un codi que faci el següent:
    # cridar a la funció block_events i guardar el resultat en una variable anomenada bloc
    # cridar a la funció chat_events i guardar el resultat en una variable anomenada missatge
    # comprovar que el bloc que hi ha a la variable 'bloc' sigui el que ha triat la màquina 
    # SI és el de la màquina -> posar pel xat "HAS ENCERTAT EL BLOC" i posar la variable start a fals
    """
        PREGUNTA 4
    """


    time.sleep(0.5)

mc.postToChat("S'ha acabat el joc")
