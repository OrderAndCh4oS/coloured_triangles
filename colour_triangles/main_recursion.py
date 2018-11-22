from colour_triangles.bulk_test_benchmark import bulk_test_benchmark
from colour_triangles.current_micro_time import current_micro_time

RGB = {'R', 'G', 'B'}


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


def triangle(row):
    """
    First Attempt
    Passes smaller tests, too much recursion to process larger strings
    :param row:
    :return:
    """
    if len(row) == 1:
        return row
    return triangle([mix_colours(row[i][-1:], row[i + 1]) for i in range(len(row) - 1)])[0]


if __name__ == '__main__':
    start = current_micro_time()
    assert triangle('RBRGBRBGGRRRBGBBBGGRBRGBRBGGRRRBGBBBGG') == 'G'
    print(current_micro_time() - start)
