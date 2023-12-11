#Quick sort complexity 0(nlogn)
def QuickSort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    pivot = array[-1]
    left = []
    right = []
    final_array = []

    for i in range(len(array) - 1):
        if array[i] <= pivot:
            left.append(array[i])
        else:
            right.append(array[i])

    final_array.extend(QuickSort(left))
    final_array.append(pivot)
    final_array.extend(QuickSort(right))

    return final_array


unsorted_list=[14,27,8,-42,11,35,-9,56,23]
sorted_list=QuickSort(unsorted_list)
print(sorted_list)

#bubble sort 
#complexity class : O(n²)
def BubbleSort(array:list[int]):
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if(array[j]>array[i]):
                temp=array[i]
                array[i]=array[j]
                array[j]=temp

BubbleSort(unsorted_list)

print(unsorted_list)