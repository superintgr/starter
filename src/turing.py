# [-1] Loading stereo perceptron state dict
left, right = load_memory("turing.pt")
# [-0] Preparing processing substrates
mid, sides = prepare_substrate(left, right)
# [+0] Restore agent model from checkpoint
agent = restore_agent(mid)
# [+1] Compute stereo perception state dict
stereo = agent.render_environment(sides)
