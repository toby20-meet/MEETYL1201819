x = input('number')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = []
for i in a:
	if i < int(x):
		list_b.append(i)

print(list_b)

