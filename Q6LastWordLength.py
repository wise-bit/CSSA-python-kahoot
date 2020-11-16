
def last_word_length(s):
	words = s.split()
	if len(words) == 0:
		return 0
	return len(words[-1])


sol = last_word_length("python is fun")
print(sol)
