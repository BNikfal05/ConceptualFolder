import time

def run_time(function):
    def get_run_time(*args, **kwargs):
        start_time_seconds = time.time()
        result = function(*args, **kwargs)
        run_speed_seconds = time.time() - start_time_seconds
        print(f"{function.__name__} run speed: {run_speed_seconds} seconds")
        return result
    
    return get_run_time

@run_time
def fast_function():
    for i in range(1000000):
        i * i

@run_time
def slow_function():
    for i in range(10000000):
        i * i

# This is how this decorator works now........
fast_function()
slow_function()
