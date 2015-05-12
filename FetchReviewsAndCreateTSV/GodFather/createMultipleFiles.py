import sys

filename = sys.argv[1].split(".tsv")[0] 

fp = open(filename +".tsv",'r')
ftitle = open(filename+"_title.tsv",'w')
freview = open(filename+"_review.tsv",'w')
freviewtitlelocation = open(filename+"_reviewtitlelocation.tsv",'w')

for line in fp: 
	splittedLine = line.split("\t")
	title = splittedLine[0].strip()	
	rating = splittedLine[1].strip()	
	location = splittedLine[2].strip()	
	review = splittedLine[3].strip()	

	ftitle.write(title +"\t "+ rating+'\n')
	freview.write(review +"\t" + rating +'\n')
	freviewtitlelocation.write(title + "\t" + location + "\t" + review + "\t" + rating+'\n')

ftitle.close()
freview.close()
freviewtitlelocation.close()
fp.close()
