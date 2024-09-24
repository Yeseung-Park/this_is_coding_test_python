# 예제. 거스름돈

N = int(input())
result = 0

for coin in [500, 100, 50, 10]:
    result += N // coin
    N %= coin

print(result)