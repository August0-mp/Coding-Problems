def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[0:n]
    else:
        i = 0
        s0 = sum(signature)
        while i+3<n:
           signature.append(s0)
           s0 += s0-signature[i]
           i += 1
    return signature