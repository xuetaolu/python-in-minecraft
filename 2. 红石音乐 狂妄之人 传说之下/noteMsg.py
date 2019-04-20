import mido

class Msg:
  def __init__(self, T=0, c=0, n=0, v=0):
    self.track    = T
    self.channel  = c
    self.note     = n
    self.velocity = v

class Msgs:
  def __init__(self):
    self.msgs = []

  def append(self, newMsg):
    self.msgs.append(newMsg)

  def hasMsgDown(self, channel, note, beside=None):
    for msg in self.msgs:
      if msg.channel == channel and msg.note == note and msg.velocity > 0 and msg != beside:
        return True
    return False

class MsgListItem:
  def __init__(self):
    self.tick = 0
    self.msgs = Msgs()

class MsgList:
  def __init__(self):
    # 最终要保存的信息表 msgList
    self.msgList = []

  def findByTick(self, tick):
    for item in self.msgList:
      if item.tick == tick:
        return item
    # 查无此项
    newItem = MsgListItem()
    newItem.tick = tick
    self.msgList.append(newItem)
    return newItem

  def fixForShortNote(self, item):
    for msg in item.msgs.msgs:
      if msg.velocity == 0 and item.msgs.hasMsgDown(channel=msg.channel, note=msg.note):
        tick = item.tick + 1
        self.findByTick(tick).msgs.append(msg)
        item.msgs.msgs.remove(msg)

  def fixForOverLapNote(self, item):
    for msg in item.msgs.msgs:
      if msg.velocity == 0 and item.msgs.hasMsgDown(channel=msg.channel, note=msg.note):
        tick = item.tick - 1
        self.findByTick(tick).msgs.append(msg)
        item.msgs.msgs.remove(msg)

  def fixForRepeatNote(self, item):
    for msg in item.msgs.msgs:
      if msg.velocity > 0 and item.msgs.hasMsgDown(channel=msg.channel, note=msg.note, beside=msg):
        item.msgs.msgs.remove(msg)

  def sortByTick(self):
    self.msgList.sort(key=lambda item: item.tick)

  def load(self, file, tickrate=20.0, restrict=0):
    mid = mido.MidiFile(file)
    currentTime = 0.0
    currentTick = 0

    lastChannel, lastNote = -1, -1
    for msg in mid:
      if msg.is_meta:
        if msg.time > 0:
          currentTime += msg.time
        
      elif msg.type == 'note_on' or msg.type == 'note_off':
        if msg.time == 0 and lastChannel == msg.channel and lastNote == msg.note and msg.velocity == 0:
          continue

        lastChannel, lastNote = msg.channel, msg.note

        currentTime += msg.time
        m = {
          'track'   : 0, #msg.track,
          'channel' : msg.channel,
          'note'    : msg.bytes()[1],
          'velocity': 0 if msg.type == 'note_off' else msg.bytes()[2],
          # 'time'    : msg.time,
          # 'tick'    : int(round(time / tickDelta)),
        }
        newMsg = Msg(m['track'],m['channel'],m['note'],m['velocity'])
        
        toTick = int(round(currentTime / (1/tickrate)))
        item = self.findByTick(toTick)
        item.msgs.append(newMsg)

        if newMsg.velocity > 0:
          self.fixForOverLapNote(item)
          self.fixForRepeatNote(item)
        else:
          self.fixForShortNote(item)

    self.sortByTick()


if __name__ == '__main__':
  msgList = MsgList()
  msgList.load(f'./mid/test.mid', 120.0 / 5)
  for item in msgList.msgList:
    print(f'tick: {item.tick}')
    for msg in item.msgs.msgs:
      if msg.velocity > 0:
        print(f'  msg: {msg.channel} {msg.note} {msg.velocity}')


          




