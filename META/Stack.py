from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  ans=0
  for i in range(N-2,-1,-1):
    if R[i]>=R[i+1]:
      R[i]=R[i+1]-1
      ans+=1
      if R[i]<=0:
        return -1
      
    
  return ans