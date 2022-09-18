import numpy as np
from numpy.testing import assert_array_equal

from chapter2 import dijkstra, warshall_floyd


def test_dijkstra():
    matrix = np.array(
        [
            [0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
        ]
    )
    vertex = 0

    expect = np.array([0, 1, 2, 2, 3, 1])
    actual = dijkstra(matrix, vertex)
    assert_array_equal(actual, expect)


def test_warshall_floyd():
    matrix = np.array(
        [
            [0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
        ]
    )
    expect = np.array(
        [
            [0, 1, 2, 2, 3, 1],
            [np.inf, 0, 1, 2, 3, np.inf],
            [np.inf, 2, 0, 1, 2, np.inf],
            [np.inf, 1, 2, 0, 1, np.inf],
            [np.inf, np.inf, np.inf, np.inf, 0, np.inf],
            [np.inf, 2, 3, 1, 2, 0],
        ]
    )
    actual = warshall_floyd(matrix)
    assert_array_equal(actual, expect)
