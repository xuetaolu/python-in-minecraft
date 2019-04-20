midiout noteopen 0 69 64
tellraw @a [{"text": "t:60, c:0, n:69, v:64", "color": "white", "bold": false}]
setblock 39 65 48 redstone_block 0 replace
midiout noteopen 0 48 64
tellraw @a [{"text": "t:60, c:0, n:48, v:64", "color": "white", "bold": false}]
setblock 39 65 27 redstone_block 0 replace
gamerule gameLoopFunction _seq:61