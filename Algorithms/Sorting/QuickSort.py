#QuickSort

def partition(arr,low,high):
	pivot=arr[high]
	i=low-1
	for j in range(low, high):
		if arr[j]<pivot:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	arr[high],arr[i+1]=arr[i+1],arr[high]
	return i+1

def quickSort(arr,low,high):
	if low<high:
		p=partition(arr,low,high)

		quickSort(arr,low,p-1)
		quickSort(arr,p+1,high)

arr=[10, 7, 8, 9, 1, 5]
l=len(arr)
quickSort(arr,0,l-1)
print(arr)