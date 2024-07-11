def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        data = func()
        end = time.time()
        print(f'время выполнения:{end - start}')
        return data

    return wrapper


@benchmark
def printtestdata():
    print('test')


@benchmark
def long_time_func():
    N = 0
    for i in range(0, 100000000):
        N = N + 1
    return N


if __name__ == '__main__':
    summa = long_time_func()
    print(summa)
