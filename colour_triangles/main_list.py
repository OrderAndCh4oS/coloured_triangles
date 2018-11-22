from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}
steps = None


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


def triangle(row):
    while len(row) > 1:
        row = [mix_colours(row[i][-1:], row[i + 1]) for i in range(len(row) - 1)]
    return row[0]


if __name__ == '__main__':
    bulk_test_benchmark(triangle)
