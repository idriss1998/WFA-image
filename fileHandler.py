from WFA import WFA
import numpy
def readWFAFromFile(filePath):
	f = open(filePath,"r")
	lines = f.readlines()
	NumberOfStats = int(lines[0])
	wfa = WFA(NumberOfStats,numpy.empty([NumberOfStats]),numpy.empty([NumberOfStats,1]),numpy.empty([4,NumberOfStats,NumberOfStats]))
	for i in range(NumberOfStats):
		wfa.I[i] = lines[1].split(" ")[i]
		wfa.F[i][0] = lines[2].split(" ")[i]
		for j in range(NumberOfStats):
			wfa.A[0][i][j] = lines[3].split(" ")[i*NumberOfStats+j]
			wfa.A[1][i][j] = lines[4].split(" ")[i*NumberOfStats+j]
			wfa.A[2][i][j] = lines[5].split(" ")[i*NumberOfStats+j]
			wfa.A[3][i][j] = lines[6].split(" ")[i*NumberOfStats+j]
	return wfa	