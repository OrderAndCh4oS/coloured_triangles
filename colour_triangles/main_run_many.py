from itertools import permutations

from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}
steps = None


def make_steps():
    global steps
    if steps == None:
        steps = {}
        for x in permutations('RRRRRGGGGGBBBBB', r=5):
            steps[x] = small_triangles(x)
    return steps


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


def small_triangles(row):
    while len(row) > 1:
        row = ''.join([mix_colours(row[i][-1:], row[i + 1]) for i in range(len(row) - 1)])
    return row


class ValidationError(Exception):
    def __init__(self, message):
        super(ValidationError, self).__init__(message)


def do_row(row, i):
    global steps
    return steps[(row[i], row[i + 1], row[i + 2], row[i + 3], row[i + 4])]


def triangle(row):
    """
    Working, but is too slow, actually slower than the original.
    Still processes the same number of items but the extra loops add to execution time
    :param row:
    :return:
    """
    if len(row) == 0:
        raise ValidationError("Row empty")
    if len(row) == 1:
        return row
    if len(row) < 8:
        return small_triangles(row)
    make_steps()
    while len(row) > 50:
        row_two = []
        row_three = []
        row_four = []
        row_five = []
        row_six = []
        row_seven = []
        row_eight = []
        row_nine = []
        row_ten = []
        for i in range(len(row) - 4):
            if i >= 0:
                row_two.append(do_row(row, i))
            if i >= 4:
                row_three.append(do_row(row_two, i - 4))
            if i >= 8:
                row_four.append(do_row(row_three, i - 8))
            if i >= 12:
                row_five.append(do_row(row_four, i - 12))
            if i >= 16:
                row_six.append(do_row(row_five, i - 16))
            if i >= 20:
                row_seven.append(do_row(row_six, i - 20))
            if i >= 24:
                row_eight.append(do_row(row_seven, i - 24))
            if i >= 28:
                row_nine.append(do_row(row_eight, i - 28))
            if i >= 32:
                row_ten.append(do_row(row_nine, i - 32))
        row = row_ten
    return small_triangles(row)


if __name__ == '__main__':
    bulk_test_benchmark(triangle)
