
# 100~200까지 짝수 합
from fcntl import I_ATMARK


arr = list(range(100,200+1)) # 100~200까지
print(arr)

sum = 0
for i in arr:
    if arr(i)%2 == 0:
        sum += i

print("sum",sum)