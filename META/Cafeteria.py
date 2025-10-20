from typing import List
# Write any import statements here

# First try: 29/32
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  nb_free = N-len(S)
  if nb_free == 0:
    return 0
  
  S = set(S)
  ans = 0
  last_seen = -K
  
  for i in range(1, N+1):
    if nb_free == 0:
      return ans
    if i in S:
      if i-last_seen < K+1:
        ans-=1
      free = 0
      last_seen = i
    else:
      if i-last_seen == K+1:
        ans+=1
        last_seen = i
      nb_free -= 1

  return ans

# Second Try:
from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  S.sort()
  S.insert(0, -K)
  S.append(N+K+1)
  
  ans = 0
  
  for i in range(1,M+2):
    gap = (S[i]-S[i-1]-K-1)//(K+1)
    if gap>0:
      ans+=gap
  return ans