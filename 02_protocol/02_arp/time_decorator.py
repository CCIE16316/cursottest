# 一个函数或者类，让其他函数或类在不需要做任何代码修改的前提下增加额外功能。
from functools import wraps
import time


def run_time_module():
    def decorator(func):
        @wraps(func)
        def print_run_time(*args, **kwargs):
            t1 = time.time()
            func_result = func(*args, **kwargs)
            t2 = time.time()
            print('本次操作时间： %.2f' % (t2 - t1))
            return func_result
        return print_run_time
    return decorator

if __name__ == '__main__':
    pass