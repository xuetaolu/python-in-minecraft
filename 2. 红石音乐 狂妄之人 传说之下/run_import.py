import midiout
import sequence
import noteMsg
import util
import random

def noteToPos(note):
  x,y,z=(39,65,0)
  return (x, y, z+note-21)

if __name__ == '__main__':
  seq = sequence.Seq()

  msgList = noteMsg.MsgList()
  msgList.load(f'./mid/test.mid', 120.0 / 5)
  for item in msgList.msgList:
    tick = item.tick
    for msg in item.msgs.msgs:
      cmd = midiout.toCmd(msg.channel, msg.note, msg.velocity)
      seq.findByTick(tick).addCmd(cmd)

      # 按下
      if msg.velocity > 0:
        seq.findByTick(tick).addCmd(util.log(f't:{tick}, c:{msg.channel}, n:{msg.note}, v:{msg.velocity}'))

        seq.findByTick(tick).addCmd(util.SetBlock(*noteToPos(msg.note), 'redstone_block').toCmd())
        
      # 弹起
      else:
        seq.findByTick(tick).addCmd(util.SetBlock(*noteToPos(msg.note), 'air').toCmd())


  seq.makeCmd(log=True)
