# Usage Guide

## `chunk_list`

Splits a list of integers into consecutive fixed-size chunks. The final chunk may be smaller than `size` if the list does not divide evenly.

### Parameters

| Parameter | Type        | Description                                      |
|-----------|-------------|--------------------------------------------------|
| `values`  | `list[int]` | The list of integers to split.                   |
| `size`    | `int`       | Maximum number of elements per chunk. Must be > 0. |

### Returns

`list[list[int]]` — A list of sublists, each containing at most `size` elements.

### Raises

- `ValueError` — if `size` is less than or equal to 0.

### Examples

```python
from exercise import chunk_list

# Even split
chunk_list([1, 2, 3, 4, 5, 6], 2)
# [[1, 2], [3, 4], [5, 6]]

# Remainder in last chunk
chunk_list([1, 2, 3, 4, 5], 3)
# [[1, 2, 3], [4, 5]]
```

---

## `moving_average`

Computes the simple moving average of a list of floats using a sliding window. Returns one average value per window position.

### Parameters

| Parameter | Type          | Description                                                              |
|-----------|---------------|--------------------------------------------------------------------------|
| `values`  | `list[float]` | The sequence of numeric values to average.                               |
| `window`  | `int`         | Number of consecutive elements per average. Must be > 0 and ≤ `len(values)`. |

### Returns

`list[float]` — A list of `len(values) - window + 1` averages, or an empty list if `window > len(values)`.

### Raises

- `ValueError` — if `window` is less than or equal to 0.

### Examples

```python
from exercise import moving_average

# 3-element window
moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3)
# [2.0, 3.0, 4.0]

# Window larger than list returns empty
moving_average([1.0, 2.0], 5)
# []
```
