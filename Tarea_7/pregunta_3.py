global b
global b_reverse
global matches
matches = 0
T = "ABRACADABRA"
#b = [0]*len(txt)
b_reverse = [0]*len(T)

def computeLPSArray(S):
	largo = 0 # length of the previous longest prefix suffix
	M = len(S)
	lps = [0]*M
	lps[0] = 0 # lps[0] is always 0
	i = 1
	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if S[i] == S[largo]:
			largo += 1
			lps[i] = largo
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if largo != 0:
				largo = lps[largo-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1
	print(lps)
	return largo

# Driver code
if __name__ == '__main__':
	S = "ABRACADABRA"
	if len(S) == 0:
		print("La cadena es vacia")
	else:
		largo = computeLPSArray(S)
		if largo == 0:
			print("La cadena es lambda")
		else:
			print({S[:largo]})
	

# This code is contributed by Bhavya Jain
