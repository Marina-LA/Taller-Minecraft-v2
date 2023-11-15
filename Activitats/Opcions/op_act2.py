import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
missatge = ""
pista = 0
llista_pistes, blocs, bloc_maquina = [], [], 0
def comprovacio(m):
    pass


#####################################################################
#                             PREGUNTA 1                            #
#####################################################################

#####
# A #
#####

block_events = mc.events.pollBlockHits()

for e in block_events:
    pos = e.pos
    bloc = mc.getBlock(pos)
    
#####
# B #
#####

def block_events():
    block_events = mc.events.pollBlockHits()

    for e in block_events:
        pos = e.pos
        return mc.getBlock(pos)

#####
# C #
#####

def block_events():
    block_events = mc.events.pollChatPosts()

    for e in block_events:
        pos = e.pos
        return mc.getBlock(pos)
    

#####################################################################
#                             PREGUNTA 2                            #
#####################################################################

#####
# A #
#####

def chat_events():
    chat_events = mc.events.pollChatPosts()

    for e in chat_events:
        return e.message
    
#####
# B #
#####

def chat_events():
    chat_events = mc.events.pollChatPosts()

    for e in chat_events:
        missatge = e.message

#####
# C #
#####

def chat_events():
    chat_events = mc.events.pollChatPosts()

    if block.DIAMOND_BLOCK == block.DIAMOND_BLOCK:
        mc.postToChat("missatge")


#####################################################################
#                             PREGUNTA 3                            #
#####################################################################

#####
# A #
#####

while pista:
    if missatge == pista:
        mc.postToChat("<maquina> SI")
    else:
        mc.postToChat("<maquina> NO")

#####
# B #
#####

if missatge == pista:
    mc.postToChat("<maquina> SI")
else:
    mc.postToChat("<maquina> NO")

#####
# C #
#####

for pista in llista_pistes:
    if missatge == pista:
        mc.postToChat("<maquina> SI")
    else:
        mc.postToChat("<maquina> NO")

#####################################################################
#                             PREGUNTA 4                            #
#####################################################################

#####
# A #
#####

bloc = block_events()
missatge = chat_events()
comprovacio(missatge)

if bloc == blocs[bloc_maquina]:
    mc.postToChat("HAS ENCERTAT EL BLOC")
    start = False

#####
# B #
#####

if bloc == blocs[bloc_maquina]:
    mc.postToChat("HAS ENCERTAT EL BLOC")
    start = False

#####
# C #
#####

block_events()
chat_events()
comprovacio(missatge)

if bloc == blocs[bloc_maquina]:
    mc.postToChat("HAS ENCERTAT EL BLOC")
    start = False