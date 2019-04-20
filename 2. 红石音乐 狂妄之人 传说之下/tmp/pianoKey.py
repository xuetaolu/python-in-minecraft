import os

# white key cmd
whiteKeyCmd = f'fill 32 64 0 39 64 87 minecraft:wool 0'

# calculate black indexs:
blackIndex = []
blackIndex.append(1)

blackSet = [1,3,6,8,10]
blackSetStartIndex = [3, 15, 27, 39, 51, 63, 75]
blackIndex.extend([i+startIndex for i in blackSet for startIndex in blackSetStartIndex])
blackIndex.sort()

def fillBlackKey(blackZ):
  return f'fill 34 64 {blackZ} 39 64 {blackZ} wool 15'

# write cmd
doc  = open(f'pianoKey.mcfunction', 'w')
cmds = '\n'.join([fillBlackKey(index) for index in blackIndex])
print(cmds)
doc.write(whiteKeyCmd + '\n' + cmds)
doc.close()

print(blackIndex)