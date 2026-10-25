import numpy as np


def standardise_loop(data):
    """Standardise each column using Python loops."""
    rows = len(data)
    cols = len(data[0])

    means = []
    stds = []

    # Har column ka mean aur standard deviation
    for j in range(cols):
        column = []

        for i in range(rows):
            column.append(data[i][j])

        mean = sum(column) / rows
        variance = sum((x - mean) ** 2 for x in column) / rows
        std = variance ** 0.5

        means.append(mean)
        stds.append(std)

    # Har element ko standardise karo
    result = []

    for i in range(rows):
        new_row = []

        for j in range(cols):
            if stds[j] == 0:
                new_row.append(0.0)
            else:
                new_row.append((data[i][j] - means[j]) / stds[j])

        result.append(new_row)

    return np.array(result)


def standardise_np(data):
    """Standardise each column using NumPy vectorisation."""
    data = np.asarray(data, dtype=float)

    means = data.mean(axis=0)
    stds = data.std(axis=0)

    # Zero standard deviation wali columns ko handle karo
    safe_stds = np.where(stds == 0, 1, stds)

    return (data - means) / safe_stds