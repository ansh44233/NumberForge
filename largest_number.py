li = list(map(int, input().split(',')))

largest = li[0]

for i in li:
    if i > largest:
        largest = i
print(largest)
