# They forgot to put in values for mass1, mass2, radius, and G

import stdio


G = 9.8
mass1 = 5
mass2 = 4
radius = 2

# They also forgot to add parenthesis around the squared part, since python doesn't follow order of operations

Force = G * mass1 * mass2 / (radius * radius)

stdio.writeln(Force)