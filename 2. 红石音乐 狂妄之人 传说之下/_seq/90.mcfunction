midiout noteclose 0 62
setblock 39 65 41 air 0 replace
midiout noteopen 0 65 64
tellraw @a [{"text": "t:90, c:0, n:65, v:64", "color": "white", "bold": false}]
setblock 39 65 44 redstone_block 0 replace
midiout noteopen 0 48 64
tellraw @a [{"text": "t:90, c:0, n:48, v:64", "color": "white", "bold": false}]
setblock 39 65 27 redstone_block 0 replace
gamerule gameLoopFunction _seq:91