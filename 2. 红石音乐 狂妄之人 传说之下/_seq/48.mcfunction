midiout noteclose 0 67
setblock 39 65 46 air 0 replace
midiout noteopen 0 60 64
tellraw @a [{"text": "t:48, c:0, n:60, v:64", "color": "white", "bold": false}]
setblock 39 65 39 redstone_block 0 replace
midiout noteopen 0 48 64
tellraw @a [{"text": "t:48, c:0, n:48, v:64", "color": "white", "bold": false}]
setblock 39 65 27 redstone_block 0 replace
gamerule gameLoopFunction _seq:49