import numpy as np

from src.marks_utils import standardise_loop, standardise_np


def test_both_functions_match():
    data = np.array([
        [10, 20, 30],
        [20, 30, 40],
        [30, 40, 50]
    ], dtype=float)

    result_loop = standardise_loop(data)
    result_np = standardise_np(data)

    assert np.allclose(result_loop, result_np)


def test_column_means_are_zero():
    data = np.array([
        [10, 20],
        [20, 40],
        [30, 60]
    ], dtype=float)

    result = standardise_np(data)

    assert np.allclose(result.mean(axis=0), [0, 0])


def test_constant_column():
    data = np.array([
        [5, 10],
        [5, 20],
        [5, 30]
    ], dtype=float)

    result = standardise_np(data)

    assert np.allclose(result[:, 0], [0, 0, 0])