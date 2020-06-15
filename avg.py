from PIL import Image
import numpy
import sys
img = Image.open("C:\\Users\\idriss\\Desktop\\python_workspace\\"+sys.argv[1])
img_array = numpy.array(img)
#new_array = numpy.empty([int(len(img_array)/2),int(len(img_array)/2),2], dtype=numpy.uint8)
somme = 0
i = 0
j = 0
while i < len(img_array):
	while j < len(img_array[i]):
		somme += int(img_array[i][j][0])
		#new_array[i][j] = img_array[i][j]
		j = j + 1
	i += 1
	j = 0	
print(int(somme/(i * i))/255)
#img = Image.fromarray(new_array)		
#img.save("C:\\Users\\idriss\\Desktop\\python_workspace\\item.png")			