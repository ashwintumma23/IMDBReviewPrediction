# Get top 10 movies of all the movies



filelist = {"review_3_Output_Location.tsv","review_51_Output_Location.tsv",  "review_54_Output_Location.tsv","review_1_Output_Location.tsv",   "review_4_Output_Location.tsv", "review_52_Output_Location.tsv",  "review_5_Output_Location.tsv","review_2_Output_Location.tsv","review_50_Output_Location.tsv", "review_53_Output_Location.tsv"}

fout = open("CombinedReviews.tsv","w")
for file in filelist:
	index = 0
	fp = open(file,'r')
	for line in fp:
		if(index < 10):
			fout.write(line)	
		index+=1
	fp.close()

fout.close()
