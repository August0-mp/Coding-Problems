from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  t = 0
  ini = 1
  
  for c in C:
      t += min(N-abs(-c+ini), abs(c-ini))
      ini = c
  return t