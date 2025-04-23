import matplotlib.pyplot as plt
import numpy as np


m = [0]
for i in range(1, 9999):
    trace = np.load(f"./traces/trace_{i:04d}.npy")
    m.append(np.mean(trace))

M = np.argmax(m)

plt.plot(m)
plt.show()