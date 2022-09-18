from logging import getLogger

import numpy as np

logger = getLogger(__name__)


def dijkstra(matrix: np.ndarray, vertex: int) -> np.ndarray:
    L = np.where(matrix == 0, np.inf, matrix)
    np.fill_diagonal(L, 0)

    n_vertices = matrix.shape[0]
    distance = np.full((n_vertices,), np.inf)

    vertices_unconfirmed = np.setdiff1d(np.arange(n_vertices), vertex)
    distance[vertex] = 0

    i = vertex
    while len(vertices_unconfirmed) > 0:
        logger.info(f"i={i}, M={vertices_unconfirmed}, d={distance}")

        for j in vertices_unconfirmed:
            distance[j] = min(distance[j], distance[i] + L[i, j])

        logger.info(f"distance updated: {distance}")

        indices = np.argsort(distance[vertices_unconfirmed])
        min_j = vertices_unconfirmed[indices[0]]
        vertices_unconfirmed = np.setdiff1d(vertices_unconfirmed, min_j)
        i = min_j

        logger.info(f"i<-{min_j}")

    return distance
