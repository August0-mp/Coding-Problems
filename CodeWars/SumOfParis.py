def sum_pairs(ints, s):
    seen = set()
    
    for x in ints:
        if s - x in seen:
            return [s - x, x]
        seen.add(x)
    
    return None