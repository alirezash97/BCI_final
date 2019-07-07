# ################################     Analytical     ################################
import numpy as np
import time
import os

start_time = time.time()
n = int(input("Please enter the number of queens: "))

solution = np.zeros((n, n), dtype=int)

if n % 2 == 1:
    solution[n-1][n-1] = 1
    n = n-1

if n % 6 != 2:

    for i in range(0, int(n/2)):
        solution[i][2*i+1] = 1

    for j in range(int(n/2), n):
        solution[j][2*j-n] = 1

if n % 6 == 2 :

    for i in range(0,int(n/2)):
        solution[i][(int(2*i+n/2)) % n] = 1

    for j in range(int(n/2), n):
        solution[j][(int(2*j-n/2+2)) % n] = 1

print(solution)

# calculate the time the program takes
total_time = time.time() - start_time
print("--------- %s seconds ---------" % total_time)

if os.path.exists("Analytical_time.txt"):
    os.remove("Analytical_time.txt")
f = open("Analytical_time.txt", "w+")
f.write(str(round(total_time, 2)))
f.close()
