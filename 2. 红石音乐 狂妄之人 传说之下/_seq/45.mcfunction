midiout noteclose 0 65
setblock 39 65 44 air 0 replace
midiout noteclose 0 50
setblock 39 65 29 air 0 replace
midiout noteopen 0 67 64
tellraw @a [{"text": "t:45, c:0, n:67, v:64", "color": "white", "bold": false}]
setblock 39 65 46 redstone_block 0 replace
gamerule gameLoopFunction _seq:46