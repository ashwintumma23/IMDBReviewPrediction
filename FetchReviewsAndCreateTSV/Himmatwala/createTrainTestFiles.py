import sys


trainFile = sys.argv[1].split(".tsv")[0] + "_train.tsv"
testFile  = sys.argv[1].split(".tsv")[0] + "_test.tsv"

ftrain = open(trainFile,"w")
ftest = open(testFile,"w")


index = 0 

fp = open(sys.argv[1],"r")
for line in fp:
	if index < 80:
		# Put line to training file
		ftrain.write(line)
	else: 
		# Put line to testing file
		ftest.write(line)
	index+=1
ftrain.close()
fp.close()
ftest.close()



