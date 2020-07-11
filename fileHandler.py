from WFA import WFA
import numpy
import struct
def readWFAFromFile(filePath):
	f = open(filePath,"rb")
	NumberOfStates = int(struct.unpack('f',f.read(4))[0])
	wfa = WFA(NumberOfStates,numpy.empty([NumberOfStates]),numpy.empty([NumberOfStates,1]),numpy.empty([4,NumberOfStates,NumberOfStates]))
	for i in range(NumberOfStates):
		wfa.I[i] = struct.unpack('f',f.read(4))[0]
	for i in range(NumberOfStates):
		wfa.F[i][0] = struct.unpack('f',f.read(4))[0]
	for a in range(4):	
		for i in range(NumberOfStates):	
			for j in range(NumberOfStates):
				wfa.A[a][i][j] = struct.unpack('f',f.read(4))[0]
	return wfa
def writeWFAInFile(wfa,fileName):
	file = open(fileName+'.wfa',"wb")
	file.write(struct.pack('f',wfa.n))
	for item in wfa.I:
		file.write(struct.pack('f',item))
	for item in wfa.F:
		file.write(struct.pack('f',item[0]))
	for a in range(len(wfa.A)):
		for i in range(len(wfa.A[a])):
			for j in range(len(wfa.A[a][i])):
				file.write(struct.pack('f',wfa.A[a][i][j]))					