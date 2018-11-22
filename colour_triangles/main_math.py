from collections import defaultdict

from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


def triangle(row):
    """
    :param row:
    :return:
    """
    if len(row) == 1:
        return row
    if len(row) == 2:
        return mix_colours(row[0], row[1])

    return find_point(row, 4)


def find_point(row, stop=1):
    while len(row) > stop:
        row = [mix_colours(row[i][-1:], row[i + 1]) for i in range(len(row) - 1)]
    return row


if __name__ == '__main__':
    result = triangle('RBRGBRBGGRRRBGBBBGGRBRGBRBGGRRRBGBBBGG')
    print(result)
    assert 'G' == result
    # bulk_test_benchmark(triangle)
