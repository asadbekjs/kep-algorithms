# text = "Aziza".lower()
# print(text[::-1] == text)
def is_palindrome_str(string):
    return string == string[::-1]

s = input().strip().lower()
print(is_palindrome_str(s))