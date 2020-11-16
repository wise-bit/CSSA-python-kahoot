def canMakeArithmeticProgression(arr):
	arr.sort()

	if len(arr) == 1:
		return True

	difference = arr[1] - arr[0]

	for i in range(len(arr)-1):
		if arr[i+1] - arr[i] != difference:
			return False

	return True