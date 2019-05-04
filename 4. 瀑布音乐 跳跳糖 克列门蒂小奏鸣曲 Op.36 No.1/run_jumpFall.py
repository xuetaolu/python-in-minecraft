import midiout
import sequence
import noteMsg
import util
import random
import math
from fallingEntity import FallingBlock
from api_piano import Piano
import time

FB = FallingBlock()

seq = sequence.Seq()

p   = Piano()

def buildPiano():
  buildCmds = []
  for note in range(21, 108+1):
    x,y,z = p.getKeyPos(note)
    kt    = p.getKeyType(note)
    if kt == 'white':
      buildCmds.append(f'fill {x} {y} {z-1} {x-10} {y} {z+1} quartz_block')
      buildCmds.append(f'fill {x} {y+1} {z-1} {x} {y+1} {z+1} stone_slab 7')
      buildCmds.append(f'fill {x} {y} {z} {x-10} {y} {z} brick_block')
      buildCmds.append(f'setblock {x} {y+1} {z} stone_slab 4')

  for note in range(21, 108+1):
    x,y,z = p.getKeyPos(note)
    kt    = p.getKeyType(note)
    if kt == 'black':
      buildCmds.append(f'fill {x} {y} {z} {x-7} {y+1} {z} nether_brick')
      buildCmds.append(f'setblock {x-7} {y+1} {z} nether_brick_stairs 0')

  util.writeMcFunction('tmp:piano', '\n'.join(buildCmds))

def buildEnd():
  buildCmds = []
  for n in range(21, 108+1):
    buildCmds.append(p.keyUp(n))
  x1,y1,z1 = p.root
  x2,y2,z2 = x1+32, y1, p.getKeyPos(108)[2]
  x3,y3,z3 = x1, y1+32+2, p.getKeyPos(108)[2]
  buildCmds.append(f'fill {x1+1} {y1} {z1} {x2} {y2} {z2} air')
  buildCmds.append(f'fill {x1} {y1+2} {z1} {x3} {y3} {z3} air')
  buildCmds.append(f'gamerule gameLoopFunction None')
  util.writeMcFunction('tmp:end', '\n'.join(buildCmds))
  
def run():
  msgList = noteMsg.MsgList()
  msgList.load(f'./mid/克列门蒂.mid', 20.0)

  for item in msgList.msgList:
    tick = item.tick
    for msg in item.msgs.msgs:
      cmd = midiout.toCmd(msg.channel, msg.note, msg.velocity)
      seq.findByTick(tick).addCmd(cmd)

      # 按下
      if msg.velocity > 0:
        # seq.findByTick(tick).addCmd(util.log(f't:{tick}, n:{msg.note} v:{msg.velocity}'))
        seq.findByTick(tick).addCmd(p.keyDown(msg.note))

        # ====== 针对按下 ========================
        # ======= 加特技 =========================
        datas=[[14,1,4], [11,9,3]] #落沙方块 data

        x,y,z = p.getKeyPos(msg.note)
        _type = p.getKeyType(msg.note)

        height = 16*math.sin(0.5*math.pi*(msg.velocity/128.0))
        org = (x-height+0.5-8,y+1,z+0.5)
        if _type == 'white':
          dst = (x-9+0.5,y+1,z+0.5)
        elif _type == 'black':
          dst = (x-6+0.5,y+2,z+0.5)
        else:
          continue

        # a. 发射第三发落沙，最后的落沙
        _org = [int(org[0])+0.5, int(org[1]), int(org[2])+0.5]
        _dst = [int(dst[0])+0.5, int(dst[1]), int(dst[2])+0.5]

        cmd, fbTick = FB.getCmdTBy2PWithTop(*_org, *_dst, y+height, 'wool', datas[msg.channel][0])
        backTick = 0 + fbTick
        seq.findByTick(tick-backTick).addCmd(cmd)

        HitEndPoint = [_org[0],_org[1]-1,_org[2]]
        HitEndTick  = backTick



        # b. 调整高度，改变源点与目标点，发射第二发落沙
        height *= 1.5
        dst = org
        org = (org[0]-height, org[1], org[2])

        _org = [int(org[0])+0.5, int(org[1]), int(org[2])+0.5]
        _dst = [int(dst[0])+0.5, int(dst[1]), int(dst[2])+0.5]

        cmd, fbTick = FB.getCmdTBy2PWithTop(*_org, *_dst, y+height, 'wool', datas[msg.channel][1])
        backTick = backTick + fbTick
        seq.findByTick(tick-backTick).addCmd(cmd)

        HitStartPoint = [_org[0],_org[1]-1,_org[2]]
        HitStartTick  = backTick

        # b(1) 可以设置垫底的黑白方块了
        _data = 0 if _type == 'white' else 15
        seq.findByTick(tick-HitStartTick).addCmd(FB.getCmdBy2PWithT(*HitStartPoint, *HitEndPoint, HitStartTick-HitEndTick, gravity=False, block='wool', data=_data)) 



        # c. 调整高度，改变源点与目标点，发射第一发落沙
        height *= 1.5
        dst = org
        org = (org[0]-height, org[1], org[2])

        _org = [int(org[0])+0.5, int(org[1]), int(org[2])+0.5]
        _dst = [int(dst[0])+0.5, int(dst[1]), int(dst[2])+0.5]

        cmd, fbTick = FB.getCmdTBy2PWithTop(*_org, *_dst, y+height, 'wool', datas[msg.channel][2])
        backTick = backTick + fbTick
        seq.findByTick(tick-backTick).addCmd(cmd)

        # ======= 加特技 =========================
        # =======  结束 ==========================


      # 弹起
      else:
        # seq.findByTick(tick).addCmd(util.log(f't:{tick}, n:{msg.note} v:{msg.velocity}'))
        seq.findByTick(tick).addCmd(p.keyUp(msg.note))

  seq.makeCmd(log=True)

if __name__ == '__main__':
  start = time.time()

  buildPiano()
  
  buildEnd()

  run()

  end = time.time()

  print(f'Used time:{end-start}')