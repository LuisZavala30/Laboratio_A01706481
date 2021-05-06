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
	"""Aplica una convolucion y devuelve la 
	matriz resultante de la operación con padding"""
	
	image_row, image_col = image.shape 		#Asigna alto y ancho de la imagen
	kernel_row, kernel_col = Filter.shape   #Asigna alto y ancho del filtro
	pad_height = int((kernel_row - 1) / 2)	#Altura de padding 
	pad_width = int((kernel_col - 1) / 2)   #Ancho de padding
	padded_image = np.zeros((image_row + (2*pad_height),image_col + (2*pad_width)))
	padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image
	padded_row, padded_col = padded_image.shape
	output_x = int((padded_row-(kernel_row/2)))	#Calcula dimension x de matriz de salida
	output_y = int((padded_col-(kernel_col/2)))	#Calcula dimension y de matriz de salida
	output = np.zeros((output_x,output_y))		#Inicializa en 0 matriz de salida

	for row in range(output_x):		#Tamaño de matriz de salida como maximo del ciclo
		for col in range(output_y):
			output[row, col] = conv_helper(padded_image[row:row + kernel_row, col:col + kernel_col],kernel)
	return output



"""Declaración de matrices y llamado a la funcion convolution"""

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



print(convolution(image,Filter))