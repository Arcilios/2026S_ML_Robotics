#!/usr/bin/env python3

# A17370336 #PID

import numpy as np
import matplotlib.pyplot as plt
import math


def computeGridSukharev(n):
    """Return X, Y coordinates of Sukharev center grid in [0,1]^2."""
    k = int(np.sqrt(n))

    if k * k != n:
        raise ValueError("n must be a perfect square.")

    X = []
    Y = []

    for i in range(k):
        for j in range(k):
            X.append((i + 0.5) / k)
            Y.append((j + 0.5) / k)

    return X, Y


def computeGridRandom(n):
    """Return X, Y coordinates of n random samples in [0,1]^2."""
    if n <= 0:
        raise ValueError("n must be positive.")

    pts = np.random.rand(n, 2)

    X = pts[:, 0]
    Y = pts[:, 1]

    return X, Y


def radical_inverse(i, base):
    """Compute radical inverse of i in given base."""
    result = 0
    f = 1 / base

    while i > 0:
        digit = i % base
        result += digit * f
        i = i // base
        f = f / base

    return result


def is_prime(b):
    """Check if b is prime."""
    if b < 2:
        return False

    for i in range(2, int(math.sqrt(b)) + 1):
        if b % i == 0:
            return False

    return True


def computeGridHalton(n, b1, b2):
    """Return X, Y coordinates of Halton sequence using bases b1 and b2."""
    if n <= 0:
        raise ValueError("n must be positive.")

    if not is_prime(b1) or not is_prime(b2):
        raise ValueError("b1 and b2 must be prime numbers.")

    if b1 == b2:
        raise ValueError("b1 and b2 must be different.")

    X = []
    Y = []

    for i in range(1, n + 1):
        X.append(radical_inverse(i, b1))
        Y.append(radical_inverse(i, b2))

    return X, Y


def plot_grid(X, Y, title):
    plt.figure(figsize=(5, 5))
    plt.scatter(X, Y)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    n = 100

    X, Y = computeGridSukharev(n)
    plot_grid(X, Y, "Sukharev Center Grid")

    X, Y = computeGridRandom(n)
    plot_grid(X, Y, "Random Grid")

    X, Y = computeGridHalton(n, 2, 3)
    plot_grid(X, Y, "Halton Sequence")