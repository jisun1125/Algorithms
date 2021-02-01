# 2021-02-01
# url : https://www.acmicpc.net/problem/1759
# 1759 암호 만들기
from itertools import combinations

l, c = map(int, input().split())  # l: 암호 길이, c: 알파벳 개수
pwd = sorted(list(input().split()))
comb = combinations(pwd, l)
sample = 'aeiou'
for c in comb:
    cnt = 0
    for i in c:
        if i in sample:
            cnt += 1

    if (cnt >= 1) and (cnt <= l-2):  # 암호 중에서 모음이 1자 이상, 자음이 2자 이상
        print(''.join(c))
