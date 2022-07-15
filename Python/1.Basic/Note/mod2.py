def sum(a, b):
    if type(a) != type(b):
        print("더하기를 할 수 없습니다.")
    else:
        return a + b

# 파이썬은 언더바2번이 시스템된다. main메소드를 선언해줘야된다.
if __name__ == "__main__":
    print(sum(10,20))
