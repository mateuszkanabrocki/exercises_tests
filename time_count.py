#!/usr/bin/env python3
import time


def count_time(function, arg):
    start = time.perf_counter()
    function(arg)
    stop = time.perf_counter()
    counted_time = stop - start
    print(f"<TIME> {str(function.__name__)}({arg}): {counted_time:.12f}")
    return counted_time 

count_time(sum, [1, 4, 6])
