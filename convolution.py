import  numpy as np

Filter = np.array([ [1,1,1],
					[0,0,0],
					[2,10,3],
	])

Matrix = np.array([	[1,2,3,0,0,0],
					[7,8,9,0,0,0],
					[0,0,1,0,0,0],
					[0,0,0,0,0,0],
					[0,0,0,0,0,0],

	])


output = np.array([	[0,0,0,0],
					[0,0,0,0],
					[0,0,0,0],
	]) 

res=0



for i in range (3):
	for j in range(3):
		MatrixAux =  np.array([Matrix[i:i+3,j:j+3]]).reshape(3,3)
		for row in range (3):
			for col in range(3):
				res = res + (MatrixAux[row,col]*Filter[row,col])
		output[i,j] = res
		res=0		

print(output)



