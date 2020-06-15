import numpy
def pixeliser(img_array,lvl=1):
	size = len(img_array)
	new_array = numpy.empty([size,size,2], dtype=numpy.uint8)
	i = 0
	j = 0
	h = 0
	k = 0
	grey = 0
	somme = 0
	while i < len(img_array):
		while j < len(img_array[i]):
			while h < 2 ** lvl:
				while k < 2 ** lvl:
					somme += int(img_array[h+i][k+j][0])
					k += 1
				k = 0	
				h += 1
			grey = int(somme/(4 ** lvl))
			somme = 0	
			h = 0
			k = 0
			while h < 2 ** lvl:
				while k < 2 ** lvl:
					new_array[h+i][k+j] = [grey,255]
					k += 1
				k = 0	
				h += 1
			h = 0
			k = 0	 
			j+=2 ** lvl
		i+=2 ** lvl
		j=0
	return new_array		
