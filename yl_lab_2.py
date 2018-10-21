import tkinter as tk
from tkinter import simpledialog

x = simpledialog.askstring("Input", "Number", parent=tk.Tk())

# x = input('number')
f = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = []
for i in f:
	if i < int(x):
		list_b.append(i)

print(list_b)
print('yo does this work fam?')
		


