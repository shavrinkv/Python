import functools,time
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        end = time.perf_counter()
        work_time = end - start
        print(f"Время {func.__name__!r}: {work_time:.4f} сек.")
        return val
    return wrapper

@timer
def test(n):
    return sum([(i/55)**2 for i in range(n)])

x = test(1000)
print(f'Результат = {x}')

