from math import log


def compute_log_loss(A):
    cross_entropy = 0
    for row in A:
        cross_entropy += (row[0] * log(row[1], 10) + ((1 - row[0]) * log(1 - row[1], 10)))

    log_loss = -1 * cross_entropy / len(A)
    return log_loss


A = [[1, 0.4], [0, 0.5], [0, 0.9], [0, 0.3], [0, 0.6], [1, 0.1], [1, 0.9], [1, 0.8]]
print(compute_log_loss(A))
