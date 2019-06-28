#SelectionSort

def SelectionSort(arr):
	l=len(arr)
	for i in range(l):
		minI=i
		for j in range(i+1,l):
			if arr[minI]>arr[j]:
				minI=j
		if minI is not i:
			arr[i],arr[minI]=arr[minI],arr[i]

arr=[10,80,30,90,40,50,70]
SelectionSort(arr)
print(arr)