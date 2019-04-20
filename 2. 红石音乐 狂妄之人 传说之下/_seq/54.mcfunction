midiout noteclose 0 60
setblock 39 65 39 air 0 replace
midiout noteopen 0 74 64
tellraw @a [{"text": "t:54, c:0, n:74, v:64", "color": "white", "bold": false}]
setblock 39 65 53 redstone_block 0 replace
midiout noteopen 0 48 64
tellraw @a [{"text": "t:54, c:0, n:48, v:64", "color": "white", "bold": false}]
setblock 39 65 27 redstone_block 0 replace
gamerule gameLoopFunction _seq:55