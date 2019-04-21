def toCmd(channel, note, velocity):
  if velocity == 0:
    return f'midiout noteclose {channel} {note}'
  else:
    return f'midiout noteopen {channel} {note} {velocity}'