import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], lw=2)

# Set limits
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Live Sine Wave Animation")
ax.set_xlabel("X (radians)")
ax.set_ylabel("sin(X)")

# Animation update function
def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 4 * np.pi, 200),
                    interval=50, blit=True, repeat=False)

plt.show()
