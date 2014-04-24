
def is_happy(n):
	while True:
		if n**2 < 10:
			return n == 1
		n = sum([int(d) ** 2 for d in str(n)])
	return False

if __name__ == '__main__':
	assert is_happy(1)
	assert not is_happy(2)
	assert is_happy(7)
	assert is_happy(10)
	assert is_happy(13)
	assert is_happy(998)
	print("OK")
