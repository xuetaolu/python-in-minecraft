midiout noteclose 0 50
setblock 39 65 29 air 0 replace
midiout noteopen 0 62 64
tellraw @a [{"text": "t:3, c:0, n:62, v:64", "color": "white", "bold": false}]
setblock 39 65 41 redstone_block 0 replace
gamerule gameLoopFunction _seq:4