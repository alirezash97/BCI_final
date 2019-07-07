import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

objects = ('evolutionary', 'Backtracking', 'Analytical')
y_pos = np.arange(len(objects))
performance = []

f = open("Evolutionary_time.txt", "r")
if f.mode == 'r':
    performance.append(float(f.read()))
f.close()

f = open("BackTracking_time.txt", "r")
if f.mode == 'r':
    performance.append(float(f.read()))
f.close()

f = open("Analytical_time.txt", "r")
if f.mode == 'r':
    performance.append(float(f.read()))
f.close()


plt.bar(y_pos, performance, align='center', alpha=0.75)
plt.xticks(y_pos, objects)
plt.ylabel('Time(seconds)')
plt.title('Total time elapsed in each algorithm')

plt.show()
