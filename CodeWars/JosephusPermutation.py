def josephus(items, k):
    it = items[:]  
    ans = []
    index = 0

    while it:
        index = (index + k - 1) % len(it)
        ans.append(it.pop(index))

    return ans

# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python