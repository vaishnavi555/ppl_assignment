book = [2,4,6,12,16,17,20,21]
for x in book:
	print(x)
print("missing page numbers are: ")
for i in range(1,26):
	if i not in book:
		print(i)

