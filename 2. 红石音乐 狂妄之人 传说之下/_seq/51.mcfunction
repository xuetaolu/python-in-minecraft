midiout noteclose 0 48
setblock 39 65 27 air 0 replace
midiout noteopen 0 60 64
tellraw @a [{"text": "t:51, c:0, n:60, v:64", "color": "white", "bold": false}]
setblock 39 65 39 redstone_block 0 replace
gamerule gameLoopFunction _seq:52