def insertionSort(arr):
   for step in range(1, len(arr)):
      key = arr[step]
      j = step -1
      
      while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j = j -1
        arr[j + 1] = key
        print(arr)
        
      print("next")



 
 
input = [9, 5, 1, 4, 3]
insertionSort(input)
print('Sorted Array in Ascending Order:')
print(input)