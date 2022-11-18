import numpy as np
import matplotlib.pyplot as plt

def mandel(x, y, size, pixels, filename):
    X = np.linspace(x, x+size, pixels)[None,:]
    Y = np.linspace(y, y+size, pixels)[:,None]
    C = X + 1j * Y
    Z = np.zeros_like(C)
    P = np.zeros_like(C, dtype='uint8')

    for i in range(120):
        print(f"Iteration {i}")
        live = np.abs(Z) < 2.
        P[live] = i 
        Z[live] = Z[live]*Z[live] + C[live] 

    plt.imshow(
        P, 
        origin='lower',
        extent=(X.min(), X.max(), Y.min(), Y.max())
    )
    plt.savefig(filename)


def mandel_zoom(old_x, new_x, old_y, new_y, old_size, new_size, pixels, num_steps):
    import numpy as np
    xs = np.linspace(old_x,new_x,num_steps)
    ys = np.linspace(old_y,new_y,num_steps)
    ds = np.linspace(old_size,new_size,num_steps)

    for i in range(num_steps):
        mandel(xs[i],ys[i],ds[i],pixels,f'zoom{i+1:02d}.png')

while True:
    try:
        pixels = input("Number of pixels: ")
        num_steps = input("Number of images: ")
        pixels = int(pixels)
        num_steps = int(num_steps)
        break
    except ValueError:
        print("Please write only integer numbers!")
        continue

mandel_zoom(-2,-0.725,-1.5,0.335,3,0.02,pixels,num_steps)
