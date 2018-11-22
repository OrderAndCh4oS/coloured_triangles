def divide_string(st):
    if not len(st) % 2:
        return st[:len(st) // 2], st[len(st) // 2:]
    else:
        return st[:len(st) // 2 + 1], st[len(st) // 2:]


if __name__ == '__main__':
    assert ("RGB", "RGB") == divide_string("RGBRGB")
    assert ("RGBG", "GRGB") == divide_string("RGBGRGB")
