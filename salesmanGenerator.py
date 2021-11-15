# import random
#
# def main():
#     graph_map = []
#     max_nodes = 100
#     for i in range(max_nodes):
#         graph_map.append([])
#     for i in range(max_nodes):
#         for j in range(max_nodes-1-i):
#             d = random.randint(1,5)
#             graph_map[i].append(d)
#             graph_map[i+j+1].append(d)
#
#     print(graph_map)
#
# if __name__ == '__main__':
#     main()

import math
import random
import numpy as np

n = 50
m = 10


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


points = [[random.randint(0, m), random.randint(0, m)] for i in range(n)]
D = np.array([[dist(points[i], points[j]) for i in range(n)] for j in range(n)])
# print(points)
print(D)

a_file = open("50.txt", "w")
for row in D:
    np.savetxt(a_file, row)
a_file.close()
