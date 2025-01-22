from threading import Thread
from random import randint
import time

class RandomThread(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        iterations = randint(1, 10)
        for _ in range(iterations):
            secs = randint(3, 10)
            print(f'Thread {self.num} sleeping {secs} seconds')
            time.sleep(secs)
        print(f'===> Thread {self.num} finished its work')

num = int(input('How many threads? '))
threads = [RandomThread(i) for i in range(1, num + 1)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    print(f'***** Thread {thread.num} "joined", i.e., is done')

print('All threads completed.')
