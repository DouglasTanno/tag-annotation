import os
import sys

# create the exit file
text_file = open("train.arff", "w")

# create the head section of .arff file
text_file.write('% Created by Douglas Tanno\n')
pathname = os.path.dirname(str(sys.argv[1])) 
text_file.write('@relation '+os.path.abspath(pathname)+'\\train.arff\n')
## write the attributes of each feature
for i in range(186):
	text_file.write('@attribute feature'+str(i+1)+' real\n')
## read the file containing the tag names, each one comma-delimited
text_file.write('@attribute output {')
with open(str(sys.argv[1])+"tags.txt") as tags_file:
	for line_tags_file in tags_file:
		text_file.write(line_tags_file)
text_file.write('}\n\n')
text_file.write('\n@data\n')


lbp = open("train-lbp.arff", "r").readlines()
acu = open("train-acu.arff", "r").readlines()

with open("train.txt","r") as t:
	song, tag = t.readline().split('\t')
	while True:
		imagePath = song
		print('Processing: '+imagePath)
		while (song == imagePath):
			text_file.write('% filename '+imagePath+'\n')

			if ('% filename '+imagePath+'\n') in acu:
				acu_ft = acu[acu.index('% filename '+imagePath+'\n')+2].split(',')
				for i in range(124):
					text_file.write(acu_ft[i])
					text_file.write(',')
				
			else:
				print('\n'+imagePath+' not found in train-acu.arff!')
				t.close()
				sys.exit()

			if ('% filename '+imagePath+'\n') in lbp:
				lbp_ft = lbp[lbp.index('% filename '+imagePath+'\n')+1].split(',')
				for i in range(62):
					text_file.write(lbp_ft[i])
					text_file.write(',')
			else: 
				print('\n'+imagePath+' not found in train-lbp.arff!')
				t.close()
				sys.exit()

			text_file.write(tag)
			print(tag)

			try:
				song, tag = t.readline().split('\t')
			except:
				print('train.arff generated!')
				t.close()
				sys.exit()


