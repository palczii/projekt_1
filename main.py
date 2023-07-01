def is_prime(n):
	if n<2:
		return False
	if n == 2:
		return True

	if n % 2 == 0:
		return False

	for i in range(3, int(n ** 0.5)+1,2):
		if n%i ==0:
			return False
	return True

for i in range(20):
	print(i, is_prime(i))



def fibo(n):
	if n in (0, 1):
		return n

	n1, n2 = 1, 0
	for i in range(n-1):
		n1, n2 = n1 + n2, n1

	return n1

print([fibo(i) for i in range(10)])

