import time

for _ in range(50):
    print(time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
    time.sleep(0.1)