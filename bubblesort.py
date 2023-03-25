#Bubble sort algorithm using python
#AUthor Ogundimu Royan

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [2,4,10,5,3,1,7,6,8,9]
newSort = bubbleSort(arr)
print ("The sorted array is: ")
for i in range(len(arr)):
    print(arr[i])