import numpy as np
from numpy.testing import assert_array_equal

from chapter2 import dijkstra


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
