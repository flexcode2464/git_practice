import time
from datetime import datetime
import sys

start_time = time.time()

while time.time() - start_time < 5:
    print(f"실시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]}", end='\r')
    sys.stdout.flush()
    time.sleep(0.1)