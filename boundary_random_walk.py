'script to generate a path sample of the boundary random walk'

import matplotlib.pyplot as plt
import math
import random
import numpy as np

# parameters to be chosen
alpha = 2
beta = 1
A = 1
B = 1
n = 300
initial_position = n//2

# jump probabilities at zero
right = (B/n**beta) / (A/n**alpha + B/n**beta)
left = (A/n**alpha) / (A/n**alpha + B/n**beta)
total = A*n**(2-alpha) + B*n**(2-beta)

positions = [initial_position]
state = initial_position
time = 0
while len(positions) < n**2:
    if state > 0:
        VarAux = math.floor(random.expovariate(1))
        positions += [state] * VarAux
        time += VarAux
        state = random.choices([state-1, state+1])[0]
    elif state == 0:
        VarAux = math.floor(n**2 * random.expovariate(total))
        positions += [state] * VarAux
        time += VarAux
        state = random.choices([-10, 1], weights=[left, right])[0]
    elif state == -10:
        redLineStartingX = len(positions)
        positions += [state] * (n**2 - time)
x = list(range(n**2))
y = positions[0:n**2]
maximumY = max(y)
yTicks = np.linspace(0, maximumY, 5, dtype='int')
margin = maximumY * 0.1
# Plot the curve
plt.plot(x, y)
# Add labels and title
plt.xlabel('time-axis')
plt.ylabel('random walk position')
plt.ylim(min(-20, -margin), maximumY + margin)
plt.yticks(yTicks, yTicks)
plt.yticks(color='w')
plt.xticks(color='w')
plt.title(
    f'RW with {n} steps, initial_position = {initial_position}, \nA = {A}, alpha = {alpha}, B = {B}, beta = {beta}')
# this highlights in red the cemetery, if it was reached
if state < 0:
    plt.hlines(y=-10, xmin=redLineStartingX, xmax=len(x),
               colors=['r'], alpha=0.3, lw=7)
# Show the plot
plt.show()
