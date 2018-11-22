from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


class ValidationError(Exception):
    def __init__(self, message):
        super(ValidationError, self).__init__(message)


def triangle(row):
    """
    Working too slow
    :param row:
    :return:
    """
    if len(row) == 0:
        raise ValidationError("Row empty")
    if len(row) == 1:
        return row
    if len(row) < 4:
        return small_triangles(row)
    while len(row) > 4:
        row = [STEPS[(row[i], row[i + 1], row[i + 2], row[i + 3])] for i in range(len(row) - 3)]
    return small_triangles(row)


if __name__ == '__main__':
    bulk_test_benchmark(triangle)
