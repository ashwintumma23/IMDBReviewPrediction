fp = open('reviews1_0','r')


fout = open('reviews1_0_Output','w')
startFlag = 0
for line in fp:
	 
	if '<h2>' in line:
		fout.write(line.strip()+'\t')
		startFlag = 1
	if '</div>' in line and startFlag==1: 
		nextLine = next(fp)
		if '<p>' in nextLine:
			newNextLine = next(fp)
			while '</p>' not in newNextLine:
				fout.write(newNextLine.strip())
				newNextLine = next(fp)
			fout.write('\n')	
		startFlag = 0 

fp.close()
fout.close()
