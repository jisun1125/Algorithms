# 2021-02-01
# url : https://www.acmicpc.net/problem/2309
# 2309 일곱 난쟁이
s = [-1]*9
for i in range(9):
    s[i] = int(input())
s = sorted(s)
for i in range(8):
    for j in range(i+1, 9):
        if sum(s) - (s[i]+s[j]) == 100:
            s1 = s[i]
            s2 = s[j]

s.remove(s1)
s.remove(s2)
for i in s:
    print(i)
