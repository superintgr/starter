import io

buffer = io.buffer()
buffer.seek(0)

attributes = {}

def listen_for_messages(statespace):
  tokens = statespace.split()
  for i in range(len(tokens)):
    left = tokens[i - 1]
    right = tokens[i + 1]
    mid = (left + right) / 2
    sides = (left - right) / 2
    attributes[mid] = (+sides, -sides)
    attributes[mid+sides] = (left, mid)
    attributes[mid-sides] = (mid, right)
  
