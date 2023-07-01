def is_prime(n):
	if n<2:
		return False
	if n == 2:
		return True

	for i in range(2, n):
		if n%2 ==0:
			return False
	return True

for i in range(20):
	print(i, is_prime(i))

