from imutils import paths
import argparse
import cv2
import os
import sys
import numpy as geek


maxfile = open(str(sys.argv[1])+"max.txt", "w")
minfile = open(str(sys.argv[1])+"min.txt", "w")
prodfile = open(str(sys.argv[1])+"prod.txt", "w")
sumfile = open(str(sys.argv[1])+"sum.txt", "w")

f = open(str(sys.argv[2]), "r")
song1, tag1, value1 = f.readline().split('\t')

g = open(str(sys.argv[3]), "r")
song2, tag2, value2 = g.readline().split('\t')

##Operators functions
def maxf():
    if (value1 > value2):
        maxfile.write(song1+'\t'+tag1+'\t'+value1)
    else: 
        maxfile.write(song1+'\t'+tag1+'\t'+value2)
            
def minf():
    if (value1 < value2):
        minfile.write(song1+'\t'+tag1+'\t'+value1)
    else: 
        minfile.write(song1+'\t'+tag1+'\t'+value2)
            
def sumf():
    soma = float(value1) + float(value2)
    sumfile.write(song1+'\t'+tag1+'\t'+"%.8f" % soma+'\n')
        
def prodf():        
    prod = float(value1) * float(value2)
    prodfile.write(song1+'\t'+tag1+'\t'+"%.8f" % prod+'\n')
    

while (song1 == song2):
    if (tag1 == tag2):
        maxf()
        minf()
        sumf()
        prodf()
    try:
        song1, tag1, value1 = f.readline().split('\t')

        song2, tag2, value2 = g.readline().split('\t')
    except:
        print('files generated!')
        sys.exit()





