midiout noteopen 0 69 64
tellraw @a [{"text": "t:12, c:0, n:69, v:64", "color": "white", "bold": false}]
setblock 39 65 48 redstone_block 0 replace
midiout noteopen 0 50 64
tellraw @a [{"text": "t:12, c:0, n:50, v:64", "color": "white", "bold": false}]
setblock 39 65 29 redstone_block 0 replace
gamerule gameLoopFunction _seq:13