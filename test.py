def compute():
    ans = max(i * j
		for i in range(100, 1000)
		for j in range(100, 1000)
		if str(i * j) == str(i * j)[ : : -1])
    return str(ans)


if __name__ == "__main__":
	print(compute())




$ string = str(a * b)
        rev = string[::-1]
        if string == rev:
            sol = string