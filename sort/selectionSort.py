def findSmallest(L):
    smallest = L[0]
    smallest_index = 0


    for i in range(1, len(L)):
        if L[i] < smallest:
            smallest = L[i]
            smallest_index = i
    return smallest_index

def selectionSort(L):
    newArr = []
    for i in range(len(L)):
        smallest = findSmallest(L)
        newArr.append(L.pop(smallest))
    return newArr

array_list = [5, 3, 2, 8, 1]

print (selectionSort(array_list))