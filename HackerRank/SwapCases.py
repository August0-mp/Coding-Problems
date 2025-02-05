def swap_case(s):
    swapped_string = ""
    for char in s:
        if 'a' <= char <= 'z':  
            swapped_string += chr(ord(char) - 32)  
        elif 'A' <= char <= 'Z':  
            swapped_string += chr(ord(char) + 32) 
        else:
            swapped_string += char  
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)