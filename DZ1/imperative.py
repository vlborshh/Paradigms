def sortImperative(array):
    for i in range(len(array)):
        max = i
        for j in range(i+1, len(array)):
            if array[j] > array[max]:
                max = j
                array[i], array[max] = array[max], array[i]
array = [0, -12, 13, -14, 15, 16]
sortImperative(array)
print(array) 