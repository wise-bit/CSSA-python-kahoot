
def merge_two_lists_inefficient(l1, l2):
	return sorted(l1 + l2) # Joins the two lists and sorts them to get ascending integers

def merge_two_lists_efficient(l1, l2):
	res = [] 
	i, j = 0, 0
		
	while i < len(l1)  and j < len(l2) : 
		if l1[i] < l2[j]: 
			res.append(l1[i]) 
			i += 1
		
		else: 
			res.append(l2[j]) 
			j += 1
		
	res = res + l1[i:] + l2[j:] 
	
	return res


sol = merge_two_lists_efficient([1, 1, 2], [1, 3, 4])
print(sol)
