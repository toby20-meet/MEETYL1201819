import random
a = []
b = []
commonlist = []
def random_list():
	x = random.randint(1,15)
	for i in range(x):
		a.append(random.randint(1,99))
	y = random.randint(1,15)
	for i in range(y)

def common():
	for i in a:
		if i in b:
			if i not in commonlist:
				commonlist.append(i)

	return(commonlist)
common()
random_list()
print(commonlist)

print(a)