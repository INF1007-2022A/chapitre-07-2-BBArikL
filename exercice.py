#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)


def get_fibonacci_sequence(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def get_sorted_dict_by_decimals(dictionary):
    return dict(sorted(dictionary.items(), key=lambda d: d[1] % 1.0))


def fibonacci_numbers(length):
    if length == 0:
        yield 0
    elif length == 1:
        yield 0
        yield 1
    else:
        yield 0
        yield 1
        seq = deque([0, 1])
        for i in range(1, length-1):
            fibo_ = seq[-1] + seq[-2]
            # new_num = last + last_last
            # last_last = last
            # last = new_num
            yield fibo_
            seq.append(fibo_)
            seq.popleft()


def build_recursive_sequence_generator(initial_values: list[int], recursive_func, keep: bool = False):
    def recursive_sequence(n: int):
        seq = deque(initial_values)

        for value in initial_values:
            n -= 1

            if n > -1:
                yield value

        for i in range(n):
            val = recursive_func(seq)

            seq.append(val)
            if not keep:
                seq.popleft()

            yield val

    return recursive_sequence


if __name__ == "__main__":
    print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
    print([get_fibonacci_number(i) for i in range(10)])
    print()

    print(get_fibonacci_sequence(1))
    print(get_fibonacci_sequence(2))
    print(get_fibonacci_sequence(10))
    print()

    spam = {
        2: 2.1,
        3: 3.3,
        1: 1.4,
        4: 4.2
    }
    eggs = {
        "foo": 42.6942,
        "bar": 42.9000,
        "qux": 69.4269,
        "yeet": 420.1337
    }
    print(get_sorted_dict_by_decimals(spam))
    print(get_sorted_dict_by_decimals(eggs))
    print()

    for fibo_num in fibonacci_numbers(10):
        print(fibo_num, end=" ")
    print("\n")


    def fibo_def(last_elems):
        return last_elems[-1] + last_elems[-2]


    fibo = build_recursive_sequence_generator([0, 1], fibo_def)

    for fi in fibo(10):
        print(fi, end=" ")
    print("\n")

    # def lucas_def(last_elems):
    #     # P = 1 et Q = -1 (??gal ?? Fibonacci)
    #     return 1*last_elems[-1] - -1*last_elems[-2]

    lucas = build_recursive_sequence_generator([2, 1], fibo_def)
    print(f"Lucas : {[elem for elem in lucas(10)]}")

    def perrin_def(last_elems: list[int]) -> int:
        return last_elems[-2] + last_elems[-3]

    perrin = build_recursive_sequence_generator([3, 0, 2], perrin_def)
    print(f"Perrin : {[elem for elem in perrin(10)]}")

    def hofq_def(last_elems: list[int]):
        n = len(last_elems)
        return last_elems[n-last_elems[n-1]] + last_elems[-last_elems[n-2]]

    hofstadter_q = build_recursive_sequence_generator([1, 1], hofq_def, keep=True)
    print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
