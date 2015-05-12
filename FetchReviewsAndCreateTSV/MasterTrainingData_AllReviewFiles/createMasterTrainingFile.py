filelist = {"review_1_Output_Location_reviewtitlelocation_train.tsv", "review_51_Output_Location_reviewtitlelocation_train.tsv",
"review_2_Output_Location_reviewtitlelocation_train.tsv",   "review_52_Output_Location_reviewtitlelocation_train.tsv",
"review_3_Output_Location_reviewtitlelocation_train.tsv",   "review_53_Output_Location_reviewtitlelocation_train.tsv",
"review_4_Output_Location_reviewtitlelocation_train.tsv" ,  "review_54_Output_Location_reviewtitlelocation_train.tsv",
"review_50_Output_Location_reviewtitlelocation_train.tsv",  "review_5_Output_Location_reviewtitlelocation_train.tsv"}

fout = open("MasterTrainingFile.tsv",'w')
for filename in filelist:

	fp = open(filename,'r')
	print "File being processed is : " + filename
	for line in fp:
		fout.write(line)
	fp.close()
fout.close()
