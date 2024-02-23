[physical annhealing]
[least power dissipation]


system = [[0, 1], [1, 0]]

state = [[1, 1], [2, 3]]

For a local state vector on which we would like the system state vector to project an image:
    - we find a matrix which maps the local state varibles to changes in the system state variables
    - for every unit change in the system parameters, the coefficient matrix will capture the gradient of the direction
         - [gradient * local state] for all unit in .
    - continue to update
