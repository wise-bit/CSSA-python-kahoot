def find_duplicate_inefficient(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] == arr[j]:
				return arr[i]
	return None


def find_duplicate_efficient(arr):
	arr.sort()
	for x in range(len(arr)-1):
		if arr[x] == arr[x+1]:
			return arr[x]
	return None


sol = find_duplicate_efficient([1, 3, 5, 4, 3, 8])
print(sol)
