import numpy as np
from sklearn.cluster import KMeans
import time
import bisect

compute_time = time.time()


def run(In: str, Out: str):
    inp = open(In, "r")
    out = open(Out, "w")

    def expend_shape(X: np.ndarray):
        if len(X.shape) > 1:
            return X
        return X.reshape(1, X.shape[0])

    def dist_ss_fast(Z: np.ndarray, X: np.ndarray):
        # Z = expend_shape(Z)
        # X = expend_shape(X)
        # Z = Z.astype("int64")
        # X = X.astype("int64")
        X2 = np.sum(X * X, 1)
        Z2 = np.sum(Z * Z, 1)
        return Z2.reshape(-1, 1) + X2.reshape(1, -1) - 2 * Z.dot(X.T)

    """
    read input 
    """
    n, K, Q = list(map(int, inp.readline().split()))
    marr = []
    for i in range(n):
        marr += [list(map(int, inp.readline().split()))]
    X = np.array(marr)
    X = X.astype("int64")

    """
    data partition
    """
    parts = []
    # print(X.shape)
    # print(X)
    for k in range(1, K + 1):
        booling = X[:, 2] == k
        part1 = X[booling, 0:2]
        part1 = sorted(part1, key=lambda x: x[0])
        part1 = np.array(part1)

        part2 = part1
        part2 = sorted(part2, key=lambda x: x[1])
        part2 = np.array(part2)

        parts.append([part1, part2])

    # print(parts[0][0], type(parts[0][0]))
    # print(parts[1])

    K_ELEMENT = 100

    def compute_in_cluster(z, part, type) -> int:
        central = bisect.bisect_right(part[:, type], z[:, type], lo=0, hi=len(part))
        ri = min(len(part), central + K_ELEMENT)
        le = max(0, central - K_ELEMENT)
        d = dist_ss_fast(z, part[le:ri])
        return np.min(d)

    for q in range(Q):
        x, y = map(int, inp.readline().split())
        z = np.array([[x, y]])
        z = z.astype("int64")
        res = 0
        for k in range(K):
            res += min(
                compute_in_cluster(z, parts[k][0], 0),
                compute_in_cluster(z, parts[k][1], 1),
            )
        out.write(str(res) + "\n")

    inp.close()
    out.close()


# run("A.inp", "A.out")
