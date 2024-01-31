
left, right = load_memory("turing.pt")

for column in zip(left, right):
    mid, sides = encode(column)
    
