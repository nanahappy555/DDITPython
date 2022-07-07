# 첫 수, 끝 수 입력. 사이의 수를 모두 더하기

a = input("첫 수를 입력하시오.")
b = input("끝 수를 입력하시오.")

aa = int(a)
bb = int(b)
sum = 0

# arr = list(range(aa,bb+1)) list() : 배열의 데이터를 출력 가능
arr = range(aa,bb+1) # 배열 범위 print(arr) => x
for i in arr :
    sum += i

print(arr) # range(2,3)이 출력됨
print(a + "부터 " + b + "까지의 합은 " + str(sum))