# def add(a, b):
#     return a + b

# print(add(5, 8))

def check_string(s):
    if s.isupper():
        return True
    elif s[0].islower() and s[1:].isupper():
        return True
    else:
        return False
    
s = input()
print(check_string(s))