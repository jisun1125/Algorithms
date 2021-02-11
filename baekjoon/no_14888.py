# 2021-02-11
# url : https://www.acmicpc.net/problem/14888
# 14888 연산자 끼워넣기
n = int(input())
a = list(map(int, input().split()))
m1, m2, m3, m4 = map(int, input().split())

sMax = -1e9
sMin = 1e9

def recursive(num, idx, add, sub, mul, div):
    global sMax, sMin
    if idx == n:
        sMax = max(num, sMax)
        sMin = min(num, sMin)
        return
    else:
        if add:
            recursive(num+a[idx], idx+1, add-1, sub, mul, div)
        if sub:
            recursive(num-a[idx], idx+1, add, sub-1, mul, div)
        if mul:
            recursive(num*a[idx], idx+1, add, sub, mul-1, div)
        if div:
            recursive(int(num/a[idx]), idx+1, add, sub, mul, div-1)

recursive(a[0], 1, m1, m2, m3, m4)
print(sMax)
print(sMin)
