"""sample workspace design"""

blocks = 512
left, right = sample_stereo(blocks)
mid, sides = encode_state(left, right)
forward = solve_for_identity(mid, -sides)
backward = solve_for_memory(mid, +sides)

attributes = {}

for block in range(blocks):
    query = forward(input("."))
    value = backward(query)
    attributes[value] = query

right, left = decode_state(attributes)
