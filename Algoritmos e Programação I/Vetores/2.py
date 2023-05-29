def insertionSort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

vector = [float(a) for a in input().split()]
divergent = 1
#print(len(set(vector)))

insertionSort(vector)

for index in range(1, len(vector)):
    if vector[index-1] != vector[index]:
        divergent += 1

if (len(vector) == 0): divergent = 0

print(divergent)
