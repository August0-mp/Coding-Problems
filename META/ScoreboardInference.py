from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  # Take the highest score: best scenatrio: all problems == 2 -> np = S[i_max]/2
  M = max(S)
  if M%2==1:
    return M//2+1
  for n in S:
    if n%2 == 1:
      return M//2+1
  return M//2