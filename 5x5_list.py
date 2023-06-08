import random
import numpy as np

ls=[]

for j in range(5):
	inner = []
	for i in range(5):
		inner.append(random.choice([0,'M']))
	ls.append(inner)

for row in range(0,5):
	for item in range(0,5):
		if ls[row][item] != 'M':
			if item != 4 and ls[row][item+1] == 'M':
				ls[row][item] += 1 
			if item != 0 and ls[row][item-1] == 'M':
				ls[row][item] += 1
			if row != 4:
				if ls[row+1][item] == 'M':
					ls[row][item] += 1
				if item != 4 and ls[row+1][item+1] == 'M':
					ls[row][item] += 1 
				if item != 0 and ls[row+1][item-1] == 'M':
					ls[row][item] += 1
			if row != 0:
				if ls[row-1][item] == 'M':
					ls[row][item] += 1
				if item != 4 and ls[row-1][item+1] == 'M':
					ls[row][item] += 1 
				if item != 0 and ls[row-1][item-1] == 'M':
					ls[row][item] += 1

for row in ls:
	print(row)

			
