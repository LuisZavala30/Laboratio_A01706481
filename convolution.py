import numpy as np
def conv_helper(fragment, kernel):
    
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result


def convolution(image,kernel):
	"""Aplica una convolucion sin padding y 
	devuelve la matriz resultante de la operación"""

	for row in range(output_x):		#Tamaño de matriz de salida como maximo del ciclo
	    for col in range(output_y):
	        output[row, col] = conv_helper(image[row:row + Filter_row, col:col + Filter_col],Filter)

	return output


Filter = np.array([ [1,1,1],	#Matriz de filtro o kernel
					[0,0,0],
					[2,10,3],
	])

image = np.array([	[1,2,3,4,5,6],		#Matriz o imagen
					[7,8,9,10,11,12],
					[0,0,1,16,17,18],
					[0,1,0,7,23,24],
					[1,7,6,5,4,3],
	])


image_row, image_col = image.shape 		#Asigna alto y ancho de la imagen
Filter_row, Filter_col = Filter.shape   #Asigna alto y ancho del filtro

output_x = int((image_row-(Filter_row/2)))	#Calcula dimension x de matriz de salida
output_y = int((image_col-(Filter_col/2)))	#Calcula dimension y de matriz de salida
output = np.zeros((output_x,output_y))		#Inicializa en 0 matriz de salida	

print(convolution(image,Filter))


