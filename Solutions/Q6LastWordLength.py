def last_word_length(s):
	s = s.strip() 
	length = 0
  
	for x in s: 
		if x == " ": 
			length = 0
		else: 
			length += 1

	return length


sol = last_word_length("python is fun")
print(sol)
