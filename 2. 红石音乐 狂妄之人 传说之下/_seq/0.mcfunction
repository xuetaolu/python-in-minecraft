midiout noteopen 0 62 64
tellraw @a [{"text": "t:0, c:0, n:62, v:64", "color": "white", "bold": false}]
setblock 39 65 41 redstone_block 0 replace
midiout noteopen 0 50 64
tellraw @a [{"text": "t:0, c:0, n:50, v:64", "color": "white", "bold": false}]
setblock 39 65 29 redstone_block 0 replace
gamerule gameLoopFunction _seq:1