import time
from datetime import datetime

start_time = time.time()

while time.time() - start_time < 5:
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-4])
    time.sleep(0.1)