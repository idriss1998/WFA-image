from PIL import Image
from test import fillImage
import numpy 
from pixeliser import pixeliser
img = Image.open("C:\\Users\\idriss\\Desktop\\python_workspace\\baby.png")
img_array = numpy.array(img)
img_array = pixeliser(img_array,4)
img = Image.fromarray(img_array)		
img.save("C:\\Users\\idriss\\Desktop\\python_workspace\\baby1.png")		 
