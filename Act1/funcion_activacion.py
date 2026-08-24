"""
	Modulo que simula el lanzamiento de una moneda.
"""
import numpy as np
N 	=	10000
CARA = 	0
CRUZ = 	0

for i in range(N):
    number = np.random.rand()
    if  number > 0.5:
        CARA = CARA + 1
    elif number <= 0.5:
        CRUZ = CRUZ + 1

print(f"Cara: {CARA}")
print(f"Cruz: {CRUZ	}")
