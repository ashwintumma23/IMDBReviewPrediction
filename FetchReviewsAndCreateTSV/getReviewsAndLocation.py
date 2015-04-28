import sys
# Read the input review HTML file
fp = open(sys.argv[1],'r')

# Open file in append mode so that other reviews can be written
fout = open(sys.argv[2],'a+')

startFlag = 0
for line in fp:
	 
	if '<h2>' in line:
		
		fout.write(line.split('<h2>')[1].strip().split('</h2>')[0].strip()+'\t')
		startFlag = 1

	elif '<b>Author' in line:
		authorLine =  next(fp)
		if '<small>' in authorLine and 'from' in authorLine:
			location = authorLine.split('from')[1].strip().split('<')[0].strip()
			print location
			fout.write(location+'\t')
		else:
			fout.write('None\t')

	elif '</div>' in line and startFlag==1: 
		nextLine = next(fp)
		if '<p>' in nextLine:
			newNextLine = next(fp)
			while '</p>' not in newNextLine:
				fout.write(newNextLine.strip()+' ')
				newNextLine = next(fp)
			fout.write('\n')	
		
		startFlag = 0	 
	else:
		print ''

fp.close()
fout.close()
