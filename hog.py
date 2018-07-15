# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

'''
codigo: http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_hog.html
versão: 0.14

se não rodar fazer o comando: pip install -U scikit-image
'''

import cv2
import os
import imutils
from skimage.feature import hog

arquivos = ["DataBase\\Nodule_x1\\Diagx1\\", "DataBase\\Nan_nodule_x1\\Diagx1\\"]

cont = 0
for path in arquivos:
	images = os.listdir(path)

	for im_file in images:
		vetor_caracteristica = []

		arq = open('pulmao.arff', 'a+')

		im_path = path + im_file
		print im_path

		im = cv2.imread(im_path)
		resized_image = imutils.resize(im, width=80, height=80)

		fd, hog_image = hog(resized_image, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualize=True,
		                    feature_vector=True)

		vetor_caracteristica.append(fd)

		row = ""
		for i in range(len(fd)):
			row += str(fd[i]) + ","

		# se é nodulo ou não:
		row += str(cont) + '\n'

		arq.write(row)
		arq.close()

	cont += 1