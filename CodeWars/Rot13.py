def rot13(message):
    ans = ""
    for c in message:
        n = ord(c)
        if n<91 and n>64:
            ans += chr(65+(n-65+13)%26)
        elif n>96 and n<123:
            ans += chr(97+(n-97+13)%26)
        else:
            ans += c
    return ans

# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python