import random
'''
a = []
b = []
commonlist = []
def random_list():
	x = random.randint(1,15)
	for i in range(x):
		a.append(random.randint(1,99))
	y = random.randint(1,15)
	for i in range(y):
		b.append(random.randint(1,99))

def common():
	for i in a:
		if i in b:
			if i not in commonlist:
				commonlist.append(i)

	return(commonlist)
random_list()
common()
print(a)
print(b)
print(commonlist)
'''
'''
import tkinter as tk
from tkinter import simpledialog

prime_numbers = 0
def is_prime(x):
	if x >=2:
		for y in range(2,x):
			if not(x%y):
				return False
	else:
		return False
	return True

for i in range(int(simpledialog.askstring("Input", "Number", parent=tk.Tk()))):
	if is_prime(i):
		print(i)