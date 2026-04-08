def solve(s):
    l = len(s)
    ans = 0
    
    for i in range(l):
        for j in range(i+1, l+1):
            if int(s[i:j])%2 == 1:
                ans+=1
    
    return ans

# https://www.codewars.com/kata/59da47fa27ee00a8b90000b4/train/python