import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12)

N_steps = 10**6 # *** Part a ***
expected_R = np.sqrt(N_steps)

repeats = 5  # *** Part b ***

ax_limit = 0 # *** Part c ***

for _ in range(repeats):  # *** Part b, indent all til plt.plot() ***
    ###################################
    #     generate one random walk    #
    ###################################
    # a list of 4 directions 0,1,2,3
    dirs = np.random.randint(0, 4, N_steps)
    # a 2D list of steps, empty for now
    steps = np.empty((N_steps,2))
    # fill the list of steps according to direction
    steps[dirs == 0] = [0,1]  # 0 - right
    steps[dirs == 1] = [0,-1] # 1 - left
    steps[dirs == 2] = [1,0]  # 2 - up
    steps[dirs == 3] = [-1,0] # 3 - down
    ###################################
    # use cumsum to sum up the individual steps to get current position
    steps = steps.cumsum(axis=0)
    ###################################
    print('Final position:',steps[-1])



    ###################################
    # draw only a selection of points, max 5000, to save memory
    skip = N_steps//5000 + 1
    xs = steps[::skip,0]
    ys = steps[::skip,1]
    maxd = np.max(np.sqrt(xs**2 + ys**2)) # *** Part d ***
    plt.plot(xs, ys, label=f'maxdist = {maxd:6.1f}')  # label: *** Part d ***
    ###################################
    
    ax_limit = max(ax_limit, np.max(np.abs(steps)))  # *** Part c ***

###################################
# add a circle with expected distance
circle = plt.Circle((0,0), radius=expected_R, color='k')
plt.gcf().gca().add_artist(circle)
# equal axis size
plt.gcf().gca().set_aspect('equal')
###################################

plt.title(f'{repeats} random walks of {N_steps} steps')  # *** Part c ***
plt.xlim(-ax_limit, ax_limit) # *** Part c ***
plt.ylim(-ax_limit, ax_limit) # *** Part c ***
plt.legend() # *** Part d ***

plt.show()
