# Script for extracting the reviews from the Positive(pos) and Negative (neg) directory

import os

# Go to the pos directory
path = r'pos'

fo = open("Review.csv", "wb")
fo.write("Reviews\n")
for file in os.listdir(path):

	# For each file in the directory, get its contents
	fp = open(path+"/"+file)
	for line in fp: 
		fo.write(line + "\n")
		

