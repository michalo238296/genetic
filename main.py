from GeneticFunctions import *
from Generator import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

BEST = ([0], 0)
print('degree of X: ')
# d = input()
print('degree of Y: ')
# d1 = input()
print('overlap-0, separate-1 :')
# overlap = input()
d = '2'
d1 = '0'
overlap = '1'
t = 0
dim = 0

if d1 == '0':
    dim = 2
else:
    dim = 3
individuals = 100
tf = []
gen = []
X = []
X1 = []

if dim == 2:
    X, X1 = Points(100, overlap, 2)  # number of points
    tf = np.arange(-4, 16, 0.1)
    gen = GenerateNew(individuals, int(d))  # number of individuals
elif dim == 3:
    X, X1 = Points(100, overlap, features=3)  # number of points
    tf = (np.arange(-4, 16, 0.1), np.arange(-4, 16, 0.1))
    gen = GenerateNew3d(individuals, int(d), int(d1))  # number of individuals

file = open('testfile.txt', 'w')
a, BEST, avg = SelectionRoulette(gen, X, X1, dim)

fig = plt.figure()
while t < 15:  # number of iterations
    a, b, avg = SelectionRoulette(gen, X, X1, dim)
    file.write(str(avg) + '\n')
    if b[1] > BEST[1]:
        BEST = b
    gen = CrossOver(a, len(gen), dim)
    gen = Mutation(gen, 10, dim)  # percent of mutation
    print('iteration:', t + 1, ', best score:', b[1], ', coefficients: ', b[0])
    plt.cla()
    if dim == 2:
        for x, x1 in zip(X, X1):
            plt.scatter(x[0], x[1], c='red')
            plt.scatter(x1[0], x1[1], c='blue')
        plt.plot(tf, f2(tf, *b[0]), 'k')
        plt.ylim(-5, 15)
        plt.pause(0.05)
        plt.cla()
    t = t + 1
print(BEST)
file.close()
if dim == 2:
    for x, x1 in zip(X, X1):
        plt.scatter(x[0], x[1], c='red')
        plt.scatter(x1[0], x1[1], c='blue')
    plt.plot(tf, f2(tf, *BEST[0]), 'g')
    plt.ylim(-5, 15)
if dim == 3:
    ax = plt.axes(projection='3d')
    for x, x1 in zip(X, X1):
        ax.scatter3D(x[0], x[1], x[2], c='red')
        ax.scatter3D(x1[0], x1[1], x1[2], c='blue')
    ax.plot_wireframe(tf[0], tf[1], np.array(f3(*tf, BEST[0][0], *BEST[0][1], *BEST[0][2])), color='black')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_zlim(-5, 15)
# print('ended coef :',BruteForce(X,X1,int(d)))
plt.show()
