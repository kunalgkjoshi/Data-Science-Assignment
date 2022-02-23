import math
S = [(1, 2), (3, 4), (-1, 1), (6, -7), (0, 6), (-5, -8), (-1, -1), (6, 0), (1, -1)]
P = (3, -4)


def closest_points_to_p(S, P):
    cosine_dist = []

    for a, b in S:
        num = a * P[0] + b * P[1]
        den = math.sqrt(a * a + b * b) * math.sqrt(P[0] * P[0] + P[1] * P[1])
        cosine_dist.append(math.acos(num / den))
    X = cosine_dist
    Y = [S for S in sorted(zip(S, X), key=lambda i: i[1])]
    k = Y[:5]
    for i, j in k:
        print(i)


closest_points_to_p(S, P)