import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

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

	if len(image.shape) == 3:							#Pasa la imagen a escala de grises
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
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
	cv2.imwrite("output_image.jpg",output)

	return output



"""Declaración de matrices y llamado a la funcion convolution"""
Filter = np.array([
	[1/9, 1/9, 1/9],
	[1/9, 1/9, 1/9],
	[1/9, 1/9, 1/9]
    ])
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"]) 



convolution(image,Filter)