#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = 0 if not tuple_a or tuple_a[0] is None else tuple_a[0]
    x2 = 0 if len(tuple_a) <= 1 or tuple_a[1] is None else tuple_a[1]

    y1 = 0 if not tuple_b or tuple_b[0] is None else tuple_b[0]
    y2 = 0 if len(tuple_b) <= 1 or tuple_b[1] is None else tuple_b[1]

    add_1 = x1 + y1
    add_2 = x2 + y2
    return (add_1, add_2)
