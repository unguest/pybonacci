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

<<<<<<< HEAD
    print(f'Time to compute the first thousand of Fibonacci\'s sequence : {stop - start} seconds')



"""
To compute the nTh term of the fibonacci sequence, we use the Binet's theorem.

	    1 + sqrt(5)
fib(n) =  ((____________)^n) / sqrt(5)
	       	 2

"""
=======
    print(f'Time to compute the first thousand of Fibonacci\'s sequence : {stop - start} seconds')
>>>>>>> ce62f9db671e5996f87dcbd83ff31c79124a0237
