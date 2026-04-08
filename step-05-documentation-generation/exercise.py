def chunk_list(values: list[int], size: int) -> list[list[int]]:
    """
    Split a list into consecutive fixed-size chunks.

    Parameters
    ----------
    values : list[int]
        The list of integers to split.
    size : int
        The maximum number of elements in each chunk. Must be greater than 0.

    Returns
    -------
    list[list[int]]
        A list of sublists, each containing at most ``size`` elements. The
        final chunk may be smaller if the list does not divide evenly.

    Raises
    ------
    ValueError
        If ``size`` is less than or equal to 0.
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    return [values[index : index + size] for index in range(0, len(values), size)]


def moving_average(values: list[float], window: int) -> list[float]:
    """
    Compute the simple moving average of a list of floats.

    Parameters
    ----------
    values : list[float]
        The sequence of numeric values to average.
    window : int
        The number of consecutive elements to include in each average.
        Must be greater than 0 and no larger than ``len(values)``.

    Returns
    -------
    list[float]
        A list of moving averages. Contains ``len(values) - window + 1``
        elements, or an empty list if ``window > len(values)``.

    Raises
    ------
    ValueError
        If ``window`` is less than or equal to 0.
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(values):
        return []
    result: list[float] = []
    for index in range(len(values) - window + 1):
        current = values[index : index + window]
        result.append(sum(current) / window)
    return result
