import numpy
import string
from PIL import Image
import math
import sys
from fileHandler import readWFAFromFile
wfa = readWFAFromFile(sys.argv[1])
def fillImage(wfa,k):
	size = 2 ** k
	new_array = numpy.empty([size,size,2], dtype=numpy.uint8)
	C = wfa.I
	x = int(0)
	y = int(0)
	resolutionInter = int((2 ** k)/2)
	i = 0
	string = ""
	while len(int2base(i,4)) < k+1:
		string = int2base(i,4)
		while len(string) < k:
			string = "0"+string
		for letter in string:
			if letter == "0":
				x = x + resolutionInter
				C = C.dot(wfa.A[0])
			elif letter == "1":
				x = x + resolutionInter
				y = y + resolutionInter
				C = C.dot(wfa.A[1])
			elif letter == "2":
				C = C.dot(wfa.A[2])	
			elif letter == "3":
				y = y + resolutionInter
				C = C.dot(wfa.A[3])
			resolutionInter = int(resolutionInter / 2)
		C = C.dot(wfa.F)
		grey = round(C[0]	* 255)
		new_array[x][y] = [grey,255]
		print("("+str(x)+","+str(y)+") "+string)
		x = int(0)
		y = int(0)
		resolutionInter	= int((2 ** k)/2)
		i = i + 1
		C = wfa.I
	return new_array


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
img_array = fillImage(wfa,int(sys.argv[3]))
img = Image.fromarray(img_array)		
img.save("/home/idriss/Documents/GitHub/WFA-image/"+sys.argv[2])