import time


def timer():
    current_time = time.localtime(time.time())
    return current_time[5]

print(timer())