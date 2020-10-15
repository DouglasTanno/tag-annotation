import os
import sys

# create the exit file
text_file = open("test.arff", "w")

# create the head section of .arff file
text_file.write('% Created by Douglas Tanno\n')
pathname = os.path.dirname(str(sys.argv[1])) 
text_file.write('@relation '+os.path.abspath(pathname)+'\\test.arff\n')
## write the attributes of each feature
for i in range(186):
	text_file.write('@attribute feature'+str(i+1)+' real\n')
## read the file containing the tag names, each one comma-delimited
text_file.write('@attribute output {test}\n\n')
text_file.write('\n@data\n')


lbp = open("test-lbp.arff", "r").readlines()
acu = open("test-acu.arff", "r").readlines()
lines = open("test.txt", "r").readlines()

for i in range(len(lines)):
	try:
		imagePath, n = lines[i].split('\n')
	except:
		imagePath = lines[i]
	print(imagePath)

	n = 1
	for n in range(2):
		text_file.write('% filename '+imagePath+'\n')
		
		if ('% filename '+imagePath+'\n') in acu:
			acu_ft = acu[acu.index('% filename '+imagePath+'\n')+2].split(',')
			for i in range(124):
				text_file.write(acu_ft[i])
				text_file.write(',')
					
		else:
			print('\n'+imagePath+'not found in test-acu.arff!')
			text_file.close()
			sys.exit()

		if ('% filename '+imagePath+'\n') in lbp:
			lbp_ft = lbp[lbp.index('% filename '+imagePath+'\n')+1].split(',')
			for i in range(62):
				text_file.write(lbp_ft[i])
				text_file.write(',')
		else: 
			print('\n'+imagePath+'not found in test-lbp.arff!')
			text_file.close()
			sys.exit()
            
		text_file.write('test\n')

print('\ntest.arff generated!')
text_file.close()
