from pyimagesearch.localbinarypatterns import LocalBinaryPatterns
import cv2
import os
import sys

# initialize the local binary patterns
points = 60
radius = 1
desc = LocalBinaryPatterns(points, radius)

# create the exit file
text_file = open(str(sys.argv[1])+"test.arff", "w")

# create the head section of .arff file
text_file.write('% Created by Douglas Tanno\n')
pathname = os.path.dirname(str(sys.argv[1]))
text_file.write('@relation '+os.path.abspath(pathname)+'\\test.arff\n')
## write the attributes of each feature
for i in range(points+2):
    text_file.write('@attribute feature'+str(i+1)+' real\n')
## read the file containing the tag names, each one comma-delimited
text_file.write('@attribute output {test}\n\n')
text_file.write('\n@data')

# read the file containing the name of the songs
f = open(str(sys.argv[1])+"test.txt", "r")
lines = f.readlines()

# loop over the testing images
for i in range(len(lines)):
    try:
        imagePath, n = lines[i].split('\n')
    except:
        imagePath = lines[i]
    print(imagePath)
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)

    e = text_file.write('\n% filename '+imagePath+'\n')

    for j in range(points+2):
        e = text_file.write(str(hist[j])+',')
    e = text_file.write('test')
    e = text_file.write('\n% filename '+imagePath+'\n')
    for j in range(points+2):
        e = text_file.write(str(hist[j])+',')
    e = text_file.write('test')

print('test.arff generated!')
f.close()