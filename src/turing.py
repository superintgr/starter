# [-1] Loading stereo perceptron state dict
left, right = load_memory("turing.pt")
# [-0] Preparing processing substrates
mid, sides = prepare_substrate(left, right)
# [+0] Restore agent model from checkpoint
agent = restore_agent(mid)
# [+1] Compute stereo perception state dict
stereo = render_environment(agent, sides)



[1, 1, 1][-1, -0, +0, +1] : [pull, forward, backward, push]
[0, 0, 0][+1, +0, -0, -1] : [push, backward, forward, pull]


class Native:
  """
  The native object has two types of identities.
  (1) cartesian,
  (2) spherical.

  Object constructor will create a pair of left-right and mid-sides varible pairs.

  [cartesian] : <left|right>
  From cartesian state vectors, the left/right is maintained around the central node.

  [spherical] : <side|mid|side>
  Within spherical coordinate space, the three dimensional vector space have components (rho, phi, theta) which maps (midpoint, psi) to (mid + sides, mid - sides).
  """
  def __init__(self):
