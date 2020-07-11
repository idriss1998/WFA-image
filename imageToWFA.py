import numpy
import string
from PIL import Image
import math
import sys
import re
import SVD
from WFA import WFA
from fileHandler import writeWFAInFile
def imageToWFA(img,Maxerror):
	Maxerror = Maxerror/10
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
	while currentState < n:
		currentImage = images[currentState]	
		for j in range(4):
			subImageF = getImageF(currentImage,j)
			new_array = getSubImage(currentImage,j)
			MatrixA = getLinearMatrix(images)
			B = getLinearMatrix([new_array])
			x = SVD.calculWeights(MatrixA,B)
			item = 0
			for i in range(len(images)):
				valX = x[i][0]
				item += valX*getImageF(images[i])
			error = math.floor(abs(item-getImageF(new_array))*10000)/100
			stateExist = False	
			if error <= Maxerror:
				stateExist = True
				for xIndex in range(len(x)):
					A[j][currentState][xIndex] = x[xIndex][0]
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
		currentState += 1
	wfa = WFA(n,I,F,A)
	return wfa

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
		return somme/((size*size)/m)/255
def getSubImage(img_array,a):
	if len(img_array) != len(img_array[0]):
		print("just w = h images !")
	elif not isPowerOfTwo(len(img_array)):
		print("just 2^k x 2^k images !")	
	else:
		size = len(img_array)
		new_array = numpy.empty([size,size,2], dtype=numpy.uint8)
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
				new_array[h+1][k] = img_array[i][j]
				new_array[h][k+1] = img_array[i][j]
				new_array[h+1][k+1] = img_array[i][j]
				j = j + 1
				k = k + 2
			i += 1
			h += 2
			j = J
			k = 0	
		return new_array				
def getLinearMatrix(images):
	A = numpy.empty([len(images[0][0]) ** 2,len(images)])
	for J in range(len(images)):
		I = 0
		img_array = images[J]
		for i in range(len(img_array)):
			for j in range(len(img_array)):
				A[I][J] = img_array[i][j][0]
				I += 1
	return A		
def Log2(x): 
    return (math.log10(x) / math.log10(2));
def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));
img = Image.open("C:\\Users\\idriss\\Documents\\GitHub\\WFA-image\\"+sys.argv[1])
wfa = imageToWFA(img,int(sys.argv[3]))
writeWFAInFile(wfa,sys.argv[2])
   
   