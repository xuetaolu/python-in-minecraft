import os
import json
import subprocess

class SetBlock:
  def __init__(self, x, y, z, block, data=0, replace=''):
    self.x, self.y, self.z, self.block, self.data, self.replace = x, y, z, block, data, replace
  def toCmd(self):
    if self.replace == '':
      return f'setblock {self.x} {self.y} {self.z} {self.block} {self.data} replace'
    else:
      return f'fill {self.x} {self.y} {self.z} {self.x} {self.y} {self.z} {self.block} {self.data} replace {self.replace}'

class Summon:
  def __init__(self, x, y, z, entity, tag=''):
    self.x, self.y, self.z, self.entity, self.tag = x, y, z, entity, tag
  def toCmd(self):
    _tag = ''
    if self.tag != None and self.tag != '':
      _tag = f' {{{self.tag}}}'
    return f'summon {self.entity} {self.x} {self.y} {self.z} {_tag}'

class TellRawNode:
  def __init__(self, text, color='white', bold=False):
    self.data = {
      "text" : text,
      "color": color,
      "bold" : bold
    }
  def toJson(self):
    return json.dumps(self.data)

class TellRaw:
  def __init__(self, entity):
    self.entity = entity
    self.nodes  = []
  def addNode(self, trNode):
    self.nodes.append(trNode)
  def toCmd(self):
    if len(self.nodes) == 0:
      return ''
    else:
      nodeJson = '[' +  ','.join([node.toJson() for node in self.nodes]) + ']'
      return f'tellraw {self.entity} {nodeJson}'

class Log:
  def __init__(self, msg):
    self.tellRaw = TellRaw('@a')
    self.tellRaw.addNode(TellRawNode(msg))
  def toCmd(self):
    return self.tellRaw.toCmd()

def log(msg):
  return Log(msg).toCmd()

def pngTellRaw(CompleteFilePath):
  # print(CompleteFilePath)
  # rc,out = subprocess.getstatusoutput(f'pngTellRaw.exe "{CompleteFilePath}"')
  # return out
  os.system(f'pngTellRaw.exe "{CompleteFilePath}"')
  with open('command.mcfunction', encoding='utf-8') as f:
    return f.read()

def writeMcFunction(name, cmd):
  namespace, _name = name.split(':')
  file = f'./{namespace}/{_name}.mcfunction'
  doc = open(file, 'w')
  doc.write(cmd)
  doc.close()
