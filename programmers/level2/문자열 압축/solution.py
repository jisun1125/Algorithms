def solution(s):
    if len(s) == 1:
        return 1
    minVal = len(s)
    for i in range(1,len(s)//2+1):
        ans = ''
        cur = s[0:i]
        curCnt = 1
        for j in range(i, len(s), i):
            if cur == s[j:j+i]:
                curCnt += 1
            else:
                if curCnt == 1:
                    ans += cur
                else:
                    ans += str(curCnt) + cur
                cur = s[j:j+i]
                curCnt = 1
        if curCnt == 1:
            ans += cur
        else:
            ans += str(curCnt) + cur
        minVal = min(minVal, len(ans))
    return minVal
