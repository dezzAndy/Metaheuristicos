import numpy as np
n 	=	10000
cara = 	0
cruz = 	0

for i in range(n):
	number = np.random.rand()
	if  number > 0.5:
		cara = cara + 1
	elif number <= 0.5:
		cruz = cruz + 1

print(f"Cara: {cara}")
print(f"Cruz: {cruz}")

