class Piano:
  def __init__(self):
    self.root = (47,64,1)
    self.bIndexs = [1, 4, 6, 9, 11, 13, 16, 18, 21, 23, 25, 28, 30, 33, 35, 37, 40, 42, 45, 47, 49, 
                    52, 54, 57, 59, 61, 64, 66, 69, 71, 73, 76, 78, 81, 83, 85]
    self.kIndexs = [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25,
                    26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48,
                    49, 50, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71,
                    72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 94, 95,
                    96, 97, 98, 99, 100, 102]
    self.kBufferL= [ []  for n in range(0, 128)]
    self.kBuffer = [ []  for n in range(0, 128)]
    self.kFlag   = [True for n in range(0, 128)]
  def getKeyType(self, note):
    if note < 21 or note > 108:
      print(f'outNote: {note}')
      return 'out'
    elif (note-21) in self.bIndexs:
      return 'black'
    else:
      return 'white'
      
  def getKeyPos(self, note):
    x,y,z = self.root
    kType = self.getKeyType(note)
    if kType != 'out':
      z += self.kIndexs[note-21]
    elif note < 21:
      z  -= (21-note)
    elif note > 108:
      z  = z+self.kIndexs[108-21] + (note-108)
    return (x,y,z)

  def keyDown(self, note):
    # self.markNote(note, channel, v=1) # 记录note

    x,y,z   = self.getKeyPos(note)
    x      -= 1
    keyType = self.getKeyType(note)
    if keyType == 'white':
      return f'execute @p {x} {y} {z} function key:whitedown'
    elif keyType == 'black':
      return f'execute @p {x} {y} {z} function key:blackdown'
    else:
      return ''

  def keyUp(self, note):
    # self.markNote(note, channel, v=0) # 记录note

    x,y,z   = self.getKeyPos(note)
    x      -= 1
    keyType = self.getKeyType(note)
    if keyType == 'white':
      return f'execute @p {x} {y} {z} function key:whiteup'
    elif keyType == 'black':
      return f'execute @p {x} {y} {z} function key:blackup'
    else:
      return ''


  def markNote(self, note, channel, v):
    self.kFlag[note] = True
    if v > 0:
      self.kBuffer[note].append(channel)
    else:
      self.kBuffer[note].remove(channel)

  def makeNoteCmd(self):
    cmds = []
    for i,flag in enumerate(self.kFlag):
      if flag:
        self.kFlag[i] = False
        maxC = 16
        last = [-1 for j in range(maxC)]
        curr = [-1 for j in range(maxC)]
        for j,c in enumerate(self.kBufferL[i]):
          last[j] = c
        for j,c in enumerate(self.kBuffer[i]):
          curr[j] = c
        for j in range(maxC):
          if curr[j] != last[j]:
            x,y,z = self.getKeyPos(i)
            x    += (j+2)
            c     = curr[j]
            if c == -1:
              cmds.append(util.SetBlock(x,y,z, 'air').toCmd())
            else:
              cmds.append(util.SetBlock(x,y,z, 'wool', (c+2)%16).toCmd())

        self.kBufferL[i] = self.kBuffer[i][:]

    return '\n'.join(cmds)