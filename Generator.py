import random
from sklearn.datasets.samples_generator import make_blobs


def GenerateNew(n, degree):
    generation = []
    for i in range(n):
        row = []
        if degree == 0:
            row = [round(random.uniform(-400, 1500))]
        elif degree == 1:
            row = [round(random.uniform(-400, 1500)), round(random.uniform(-2047, 2047))]
        elif degree == 2:
            row = [round(random.uniform(-400, 1500)), round(random.uniform(-2047, 2047)),
                   round(random.uniform(-2047, 2047))]
        elif degree == 3:
            row = [round(random.uniform(-400, 1500)), round(random.uniform(-2047, 2047)),
                   round(random.uniform(-2047, 2047)), round(random.uniform(-2047, 2047))]
        elif degree == 4:
            row = [round(random.uniform(-400, 1500)), round(random.uniform(-2047, 2047)),
                   round(random.uniform(-2047, 2047)), round(random.uniform(-2047, 2047)),
                   round(random.uniform(-2047, 2047))]
        elif degree == 5:
            row = [round(random.uniform(-400, 1500)), round(random.uniform(-2047, 2047)),
                   round(random.uniform(-2047, 2047)), round(random.uniform(-2047, 2047)),
                   round(random.uniform(-2047, 2047)), round(random.uniform(-2047, 2047))]
        generation.append(row)
    return generation


def GenerateNew3d(n, xdegree, ydegree):
    generation = []
    for i in range(n):
        row = []
        row.append(random.randint(-400, 1500))
        temp = []
        for x in range(xdegree):
            temp.append(random.randint(-2047, 2047))
        row.append(temp)
        temp = []
        for y in range(ydegree):
            temp.append(random.randint(-2047, 2047))
        row.append(temp)
        generation.append(row)
    return generation


def Points(n, o, features):
    if int(o):
        X, y = make_blobs(n_samples=n, centers=None, n_features=features, random_state=0, center_box=(10, 10),
                          cluster_std=2)
        X1, y1 = make_blobs(n_samples=n, centers=None, n_features=features, random_state=0, center_box=(2, 2),
                            cluster_std=2)
    else:
        X, y = make_blobs(n_samples=n, centers=None, cluster_std=5, n_features=features, random_state=0,
                          center_box=(10, 10))
        X1, y1 = make_blobs(n_samples=n, centers=None, cluster_std=5, n_features=features, random_state=0,
                            center_box=(2, 2))
    return X, X1
