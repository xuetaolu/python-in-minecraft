midiout noteclose 0 62
setblock 39 65 41 air 0 replace
midiout noteopen 0 74 64
tellraw @a [{"text": "t:6, c:0, n:74, v:64", "color": "white", "bold": false}]
setblock 39 65 53 redstone_block 0 replace
midiout noteopen 0 50 64
tellraw @a [{"text": "t:6, c:0, n:50, v:64", "color": "white", "bold": false}]
setblock 39 65 29 redstone_block 0 replace
gamerule gameLoopFunction _seq:7