import numpy
def crop(img_array,size)
	new_array = numpy.empty([size,size,2], dtype=numpy.uint8)
	i = 0
	j = 0
	while i < len(new_array):
		while j < len(new_array[i]):
			new_array[i][j] = img_array[i][j]
			j += 1
		i += 1
		j = 0
	return new_array		