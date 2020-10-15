from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import os
import sys
import numpy as geek


text_file = open("max.txt", "w")

f = open("lbp.txt", "r")
musica1, tag1, valor1 = f.readline().split('\t')


g = open("acu.txt", "r")
musica2, tag2, valor2 = g.readline().split('\t')

while (musica1 == musica2):
    if (tag1 == tag2):
        if (valor1 > valor2):
            text_file.write(musica1+'\t'+tag1+'\t'+valor1)
        else: 
            text_file.write(musica1+'\t'+tag1+'\t'+valor2)
    try:
        musica1, tag1, valor1 = f.readline().split('\t')

        musica2, tag2, valor2 = g.readline().split('\t')
    except:
        print('Arquivo max gerado!')
        sys.exit()



