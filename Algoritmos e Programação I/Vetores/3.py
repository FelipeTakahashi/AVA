vector = [str(a) for a in input().split()]
found = False
find = str(input())

for index in range(len(vector)):
    if (vector[index] == find):
        found = True
        print(f"{find} found at index: {index}")

if not found:
    print("-1")
