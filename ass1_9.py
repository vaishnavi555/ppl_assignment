x = 1
y = 1
num = 0
l1 = []
den = 0
while x < 10:
	while y != 0:
		no = y
		if no % y == 0:
			num = num + 1
			l1.append(no)
	
		else: 
			y = y - 1
	nume = num
	for a in range(num):
		b = l1[a]
		c = 1/b
		den = den + c
	res = nume/den
	if(isinstance(res,int)):
		x = x + 1
		y = y + 1
		print(res)
	else:
		y = y + 1
