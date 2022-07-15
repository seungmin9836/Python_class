PI = 3.141592

# 파이썬은 함수를 선언할때 self가 꼭 있어야된다.
class Math:
    def solve(self, r):
        return PI * (r**2)
    def sum(self, a, b):
        return a + b

# ---- 여기까지는 reference(참고) 이다.
# ---- 밑으로부터는 실행하는 구간

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solve(2))
    print(a.sum(PI, 4.4))