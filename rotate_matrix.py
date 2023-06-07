import numpy as np

def rotate_matrix(square_matrix):
	'''Takes in 2d square matrix, returns its 180 degrees rotated matrix'''
	if square_matrix.shape[0] != square_matrix.shape[1]:
		print('Error : the matrix should have equal rows and columns.') 
	else:
		matrix_shape = (square_matrix.shape)
		square_matrix = square_matrix.flatten()
		result = np.arange(square_matrix.size)
		for i in range(len(square_matrix)):
			result[0] = square_matrix [-1]
			result[i] = square_matrix[-i-1]
		result = result.reshape(matrix_shape)
		print(result)

arr = np.arange(1,17)
arr = arr.reshape(4,4)
rotate_matrix(arr)