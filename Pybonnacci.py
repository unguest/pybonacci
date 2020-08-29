#!/usr/bin/env python3
#coding:utf-8

import sys
import math
import time


def fibonacci(n):
    return round((((1 + math.sqrt(5)) / 2)**n) / math.sqrt(5))

if __name__ == "__main__":

    fib = lambda n: round((((1 + math.sqrt(5)) / 2)**n) / math.sqrt(5))
    start = time.time()
    for i in range(1000):
        print(fib(i))
    stop = time.time()

    print(f'Time to compute the first thousand of Fibonacci\'s sequence : {stop - start} seconds')