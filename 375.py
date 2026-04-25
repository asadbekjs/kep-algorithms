n = int(input())
a = list(map(int, input().split()))
max_index = a.index(max(a))
min_index = a.index(min(a))

print(abs(max_index - min_index) - 1)