# Before

total1 = 0

for i in range(0,100000000):
    total1 += i
print(total1)

# After
    # Thread란? : 한문제를 가지고 다른 cpu가 같이 작업을 나눠서 계산
from threading import Thread
def calc(start, end):
    total = 0
    for i in range(start, end):
        total += i
    print(total1)

if __name__ == "__main__":
    start, end = 0, 100000000
    thr1 =  Thread(target=calc, args=(start, end))

    thr1.start()
    thr1.join()