from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
import cv2
import os
import sys

# initialize the local binary patterns
points = 60
radius = 1
desc = LocalBinaryPatterns(points, radius)

# create the exit file
text_file = open(str(sys.argv[1])+"train.arff", "w")

# create the head section of .arff file
text_file.write('% Created by Douglas Tanno\n')
pathname = os.path.dirname(str(sys.argv[1])) 
text_file.write('@relation '+os.path.abspath(pathname)+'\\train.arff\n')
## write the attributes of each feature
for i in range(points+2):
	text_file.write('@attribute feature'+str(i+1)+' real\n')
## read the file containing the tag names, each one comma-delimited
text_file.write('@attribute output {')
with open(str(sys.argv[1])+"tags.txt") as t:
        for line in t:
            text_file.write(line)
text_file.write('}\n\n')
text_file.write('\n@data\n')

# read the file containing the name of the songs
# plus their respective tags
f = open(str(sys.argv[1])+"train.txt", "r")
song, tag = f.readline().split('\t')
imagePath = song
print(imagePath)

# loop over the training images
while(imagePath):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	hist = desc.describe(gray)
    
	while (song == imagePath):
		e = text_file.write('% filename '+imagePath+'\n')
			
		for i in range(points + 2):
			e = text_file.write(str(hist[i])+',')
			
		e = text_file.write(tag)
		try:
			song, tag = f.readline().split('\t')
		except:
			print('train.arff generated!')
			f.close()
			sys.exit()
	imagePath = song
	print(imagePath)