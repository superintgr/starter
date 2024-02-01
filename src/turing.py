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
  
  Universal properties:
  - native * native ~ super(native); which is an union of two instances with same constructive/destructive properties.

  Beats instead of clocks:
  Two instaces having different substrate properties will cause their mixture to produce beat waves, before synchronizing to their medium variables.
  
  """
  def __init__(self):
    self.left =  [[1, 1, 1],
                  [1, 1, 0],
                  [1, 0, 0]]
    self.right = [[0, 0, 1],
                  [0, 1, 1],
                  [1, 1, 1]]
    self.mid =   [[0, 1/2], [-1/2, -1]]
    self.sides = [[0, -1/2], [1/2, 0]]

  def __add__(self, other):
    pass

[@ group theory: noether's theorem]
[-1] conservation law
[-0] preserved symmetry
[+0] conserved quantity
[+1] differentiable action



[@ duality, wave function, audible phenomenon, universality: encoder/decoder]
[-1] cartesian (x, y, z) coordinates although reveal where an object might be in a scaled geometric space, however do not tell us how any changes to position of those objects come about.
[-0] spherical (magnitude, angle, orientation) coordinates do reveal how each cartesian derivatives come about as they change from one to others.
[+0] it could be looked at as (unattendended dynamical changes to globally visible information variables), and (attending in counterpart process actively so that the motion required for changes to be external gets computed through locally accessible variables).
[+1] in short, it could be said that whichever information is not locally accessible to a driver dealing with implicit information causing spherical-cartesian to swap phases, those such variables are computation variables whose medium contains locally accessible information.
[1-] More clearly it is the static/dynamic swapping process between at least two 2-level systems whose attributes are entangled with each other through union operations and whose intersecting subsets are bound to be within the two objects' combined set of possible attributes.
[0-] For any cartesian vector, the corresponding line connecting the origin to the star whose position requires a theta angle displacement from the vertical line (z) and straight projection of the feature (star) onto the horizontal plane where the front of the face have a total of 180 degrees of freedom (90 from midpoint (nose/center of forehead/perpendicular bi-section etc.) in left-right side directions) and the head orientation is such that the projected perpendicular line lands on the possible azimuth coverage through stereographic view.
[0+] using triangle inequality, many components of the geometric configurations could let us solve for any missing variable 
[1+] for example, if a source can detect a star using (x, y, z) positional vector as target point from some source vector, as long as both source and target object remain in existance, given the constraint on the dynamical parameters such as step sizes, gravity, conservation of physical quantities, grid/graph networks etc., the o
corresponding solution set is constructable.



[@ pritoms: new workspace]
[-1] i have found the graphing and diagramming tool {?} very useful
[-0] even through it is a huge cartesian plane, it has many points to expand deep
[+0] i can draw my entire workplan in that environment, so what is left after the drawing must be done else where
[+1] perhaps I can turn the drawings into graphs and networks, then implement straight-up network graphs as programs
