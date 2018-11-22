from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}
memo = {}
rows = {}


def mix_colours(a, b):
    try:
        return memo[(a, b)]
    except KeyError:
        result = b if a == b else next(iter(RGB ^ {a, b}))
        memo[(a, b)] = result
        return result


def small_triangles(row):
    row_key = tuple(row)
    try:
        return memo[row_key]
    except KeyError:
        row = mix_row(row)
        memo[row_key] = row
        return row


def mix(row):
    if len(row) == 1:
        return row
    key = tuple(row)
    try:
        return mix(rows[key])
    except KeyError:
        row = ''.join([mix_colours(row[i][-1:], row[i + 1]) for i in range(len(row) - 1)])
        rows[key] = row
        return mix(row)


def mix_row(row, key=None):
    if len(row) == 1:
        memo[key] = row
        return row
    if key is None:
        key = tuple(row)
    try:
        return mix_row(memo[key], key)
    except KeyError:
        result = mix(row)
        return mix_row(result, key)


class ValidationError(Exception):
    def __init__(self, message):
        super(ValidationError, self).__init__(message)


def triangle(row):
    """
    Working still too slow, but faster
    :param row:
    :return:
    """
    if len(row) == 0:
        raise ValidationError("Row empty")
    if len(row) == 1:
        return row
    while len(row) > 9:
        row = [small_triangles(row[i:i + 9]) for i in range(len(row) - 8)]
    return small_triangles(row)


if __name__ == '__main__':
    bulk_test_benchmark(triangle)
