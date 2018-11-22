from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}
STEPS = {('R', 'B', 'G', 'R'): 'R', ('B', 'B', 'G', 'G'): 'R', ('R', 'R', 'G', 'G'): 'B', ('G', 'R', 'B', 'G'): 'G',
         ('G', 'G', 'R', 'R'): 'B', ('B', 'G', 'B', 'G'): 'R', ('R', 'B', 'R', 'G'): 'B', ('B', 'G', 'G', 'R'): 'G',
         ('B', 'B', 'R', 'R'): 'G', ('G', 'R', 'B', 'B'): 'R', ('B', 'B', 'B', 'R'): 'G', ('B', 'R', 'R', 'R'): 'G',
         ('G', 'B', 'G', 'B'): 'R', ('B', 'R', 'R', 'G'): 'R', ('B', 'B', 'G', 'B'): 'B', ('R', 'G', 'R', 'R'): 'R',
         ('B', 'R', 'G', 'R'): 'G', ('R', 'B', 'R', 'R'): 'R', ('R', 'G', 'G', 'G'): 'B', ('R', 'G', 'B', 'R'): 'R',
         ('B', 'B', 'R', 'G'): 'R', ('R', 'B', 'G', 'G'): 'B', ('R', 'R', 'G', 'R'): 'R', ('R', 'G', 'G', 'R'): 'R',
         ('B', 'G', 'R', 'R'): 'G', ('R', 'R', 'B', 'G'): 'B', ('G', 'G', 'G', 'G'): 'G', ('G', 'R', 'G', 'R'): 'B',
         ('R', 'B', 'B', 'G'): 'B', ('G', 'B', 'R', 'B'): 'R', ('B', 'R', 'G', 'B'): 'B', ('B', 'B', 'B', 'B'): 'B',
         ('G', 'G', 'G', 'R'): 'B', ('B', 'B', 'B', 'G'): 'R', ('G', 'B', 'B', 'B'): 'R', ('G', 'G', 'B', 'B'): 'R',
         ('R', 'R', 'R', 'B'): 'G', ('B', 'R', 'B', 'B'): 'B', ('R', 'B', 'B', 'B'): 'G', ('G', 'G', 'G', 'B'): 'R',
         ('B', 'B', 'G', 'R'): 'G', ('R', 'R', 'B', 'B'): 'G', ('G', 'B', 'R', 'R'): 'B', ('B', 'R', 'B', 'G'): 'R',
         ('R', 'G', 'B', 'G'): 'B', ('R', 'R', 'R', 'R'): 'R', ('B', 'G', 'G', 'B'): 'B', ('G', 'B', 'G', 'G'): 'G',
         ('B', 'G', 'R', 'B'): 'B', ('R', 'G', 'B', 'B'): 'G', ('R', 'B', 'R', 'B'): 'G', ('G', 'G', 'R', 'G'): 'G',
         ('B', 'R', 'B', 'R'): 'G', ('G', 'R', 'R', 'R'): 'B', ('B', 'B', 'R', 'B'): 'B', ('B', 'R', 'R', 'B'): 'B',
         ('G', 'B', 'G', 'R'): 'B', ('G', 'B', 'B', 'G'): 'G', ('G', 'G', 'B', 'G'): 'G', ('G', 'R', 'B', 'R'): 'B',
         ('G', 'R', 'R', 'B'): 'R', ('G', 'B', 'R', 'G'): 'G', ('R', 'B', 'B', 'R'): 'R', ('B', 'R', 'G', 'G'): 'R',
         ('R', 'G', 'R', 'B'): 'G', ('G', 'G', 'R', 'B'): 'R', ('R', 'R', 'B', 'R'): 'R', ('R', 'R', 'R', 'G'): 'B',
         ('R', 'B', 'G', 'B'): 'G', ('R', 'G', 'R', 'G'): 'B', ('B', 'G', 'R', 'G'): 'R', ('G', 'R', 'G', 'G'): 'G',
         ('R', 'R', 'G', 'B'): 'G', ('G', 'R', 'R', 'G'): 'G', ('R', 'G', 'G', 'B'): 'G', ('B', 'G', 'B', 'B'): 'B',
         ('B', 'G', 'G', 'G'): 'R', ('G', 'B', 'B', 'R'): 'B', ('G', 'R', 'G', 'B'): 'R', ('G', 'G', 'B', 'R'): 'B',
         ('B', 'G', 'B', 'R'): 'G'}


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


def small_triangles(row):
    while len(row) > 1:
        row = ''.join([mix_colours(row[i][-1:], row[i + 1]) for i in range(len(row) - 1)])
    return row


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
