
def twoSumInefficient(nums, target):

	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]
	return None


def twoSumEfficient(nums, target):

	pair = {}

	for i in range(len(nums)):
		if target - nums[i] in pair:
			return [pair[target - nums[i]], i]
		else:
			pair[nums[i]] = i

	return None
