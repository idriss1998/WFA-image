import numpy
import string
from PIL import Image
import math
import sys
import re
def imageToWFA(img):
	logiqualRegex1 = re.compile('^0*10*$')
	logiqualRegex2 = re.compile('^[0|2|3]+$')
	img = img.convert('LA')
	img_array = numpy.array(img)
	n = 1
	currentState = n - 1
	images = [img_array]
	I = [1]
	F = [[0]]
	A = [[[0]],[[0]],[[0]],[[0]]]
	F[0][0] = getImageF(img_array)
	I[0] = 1
	i = 1
	string = ""
	currentImage = images[currentState]
	while currentState < n:
		currentImage = images[currentState]	
		for j in range(4):
			subImageF = getImageF(currentImage,j)
			new_array = getSubImage(img_array,j)
			img = Image.fromarray(new_array)
			img.save("/home/idriss/Documents/GitHub/WFA-image/test"+str(j)+".png")
			while len(int2base(i,4)) < n+1:
				string = int2base(i,4)
				while len(string) < n:
					string = "0"+string	
				item = 0
				stateExist = False		
				# 0 for 0
				# 1 for 1
				# 2 for 0.5
				# 3 for 0.25
				for letterIndex in range(len(string)):
					if string[letterIndex] == "1":
						item += F[letterIndex][0]
					elif string[letterIndex] == "2":
						item += 0.5*F[letterIndex][0]	
					elif string[letterIndex] == "3":
						item += 0.25*F[letterIndex][0]
				#print(str(j)+" "+string+" "+str(item))
				boolean = False				
				if subImageF == item and (logiqualRegex1.match(string) or logiqualRegex2.match(string)):
					if logiqualRegex1.match(string):
						for l in range(4):
							if getImageF(currentImage,l) != getImageF(images[string.index('1')],l):
								boolean = True
					if boolean:
						break			
					stateF = item
					stateExist = True
					for letterIndex in range(len(string)):
						if string[letterIndex] == "0":
							A[j][currentState][letterIndex] = 0
						elif string[letterIndex] == "1":
							A[j][currentState][letterIndex] = 1
						elif string[letterIndex] == "2":
							A[j][currentState][letterIndex] = 0.5
						elif string[letterIndex] == "3":
							A[j][currentState][letterIndex] = 0.25
					print(str(currentState+1)+" "+str(j)+" "+string+" "+str(item))
					break							
					
				i = i + 1
			if subImageF != 0.0 and stateExist == False:
				n += 1
				J = 0	
				while J < 4:
					A[J].append([0])
					for H in range(len(A[J])):
						while len(A[J][H]) < n:
							A[J][H].append(0)
					J += 1	
				I.append(0)
				F.append([subImageF])
				A[j][currentState][n-1] = 1
				newImage = getSubImage(currentImage,j)
				images.append(newImage)
			i = 1
		currentState += 1
	#print(A[int(sys.argv[1])])
	stringFile = str(n)+"\n"
	for item in I:
		stringFile += str(item)+" "
	stringFile += "\n"
	for item in F:
		stringFile += str(item[0])+" "
	stringFile += "\n"
	for a in range(len(A)):
		for i in range(len(A[a])):
			for j in range(len(A[a][i])):
				stringFile += str(A[a][i][j])+" "
		stringFile += "\n"			
	file = open(sys.argv[2],"w")
	file.write(stringFile)



digs = string.digits + string.ascii_letters
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

def getImageF(img_array,a=-1):
	if len(img_array) != len(img_array[0]):
		print("just w = h images !")
	elif not isPowerOfTwo(len(img_array)):
		print("just 2^k x 2^k images !")	
	else:
		size = len(img_array)
		m = 4
		if a == -1:
			m = 1
			i = 0
			J = 0
			sizeI = size
			sizeJ = size
		elif a == 0:
			i = int(size/2)
			J = 0
			sizeI = size
			sizeJ = int(size/2)
		elif a == 1:
			i = int(size/2)
			J = int(size/2)
			sizeI = size
			sizeJ = size
		elif a == 2:
			i = 0
			J = 0
			sizeI = int(size/2)
			sizeJ = int(size/2)
		elif a == 3:
			i = 0
			J = int(size/2)
			sizeI = int(size/2)
			sizeJ = size
		else:
			print("a is not in sigma")
		somme = 0
		j = J	
		while i < sizeI:
			while j < sizeJ:
				somme += int(img_array[i][j][0])
				j = j + 1
			i += 1
			j = J	
		return math.floor((somme/((size*size)/m)/255)*100)/100
def getSubImage(img_array,a):
	if len(img_array) != len(img_array[0]):
		print("just w = h images !")
	elif not isPowerOfTwo(len(img_array)):
		print("just 2^k x 2^k images !")	
	else:
		size = len(img_array)
		newSize = int(size / 2)
		new_array = numpy.empty([newSize,newSize,2], dtype=numpy.uint8)
		h = 0
		k = 0
		if a == 0:
			i = int(size/2)
			J = 0
			sizeI = size
			sizeJ = int(size/2)
		elif a == 1:
			i = int(size/2)
			J = int(size/2)
			sizeI = size
			sizeJ = size
		elif a == 2:
			i = 0
			J = 0
			sizeI = int(size/2)
			sizeJ = int(size/2)
		elif a == 3:
			i = 0
			J = int(size/2)
			sizeI = int(size/2)
			sizeJ = size
		else:
			print("a is not in sigma")
		somme = 0
		j = J	
		while i < sizeI:
			while j < sizeJ:
				new_array[h][k] = img_array[i][j]
				j = j + 1
				k = k + 1
			i += 1
			h += 1
			j = J
			k = 0	
		return new_array				

def Log2(x): 
    return (math.log10(x) / math.log10(2));
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));
img = Image.open("/home/idriss/Documents/GitHub/WFA-image/"+sys.argv[1])
imageToWFA(img)    
   