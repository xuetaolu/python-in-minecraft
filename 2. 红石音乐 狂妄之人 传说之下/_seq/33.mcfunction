midiout noteopen 0 65 64
tellraw @a [{"text": "t:33, c:0, n:65, v:64", "color": "white", "bold": false}]
setblock 39 65 44 redstone_block 0 replace
midiout noteopen 0 50 64
tellraw @a [{"text": "t:33, c:0, n:50, v:64", "color": "white", "bold": false}]
setblock 39 65 29 redstone_block 0 replace
gamerule gameLoopFunction _seq:34