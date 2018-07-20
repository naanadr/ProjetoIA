import os
import cv2
import random
import shutil

arquivos = ["DataBase\\Nodule_x1\\Diagx1\\", "DataBase\\Nan_nodule_x1\\Diagx1\\"]

vetor_aux = []

for path in arquivos:
	local = os.listdir(path)

	for im_file in local:
		string = path + im_file
		vetor_aux.append(string)

vetor_aux2 = []
for arquivo in vetor_aux:
	img = cv2.imread(arquivo)

	if 'Nodule_x1' in arquivo:
		novo = 'nodule' + arquivo.split('diagx11')[1]
	elif 'Nan_nodule_x1' in arquivo:
		novo = 'nannodule' + arquivo.split('diagx11')[1]

	vetor_aux2.append(novo)
	cv2.imwrite("DataBase\\Total\\" + novo, img)


local_antigo = "DataBase\\Total\\"
local_teste = "DataBase\\Teste\\"
local_treinamento = "DataBase\\Treinamento\\"

arquivos = os.listdir(local_antigo)
total_arquivos = len(arquivos)

random.shuffle(vetor_aux2)

quantid_treinamento = total_arquivos * 2/3
posicao_teste = total_arquivos * 1/3

for pos in range(quantid_treinamento+1):
	arquivo_completo_antigo = local_antigo + vetor_aux2[pos]
	arquivo_completo_novo = local_treinamento + vetor_aux2[pos]

	shutil.move(arquivo_completo_antigo, arquivo_completo_novo)

lim1 = quantid_treinamento+1
for pos in range(lim1, total_arquivos):
	arquivo_completo_antigo = local_antigo + vetor_aux2[pos]
	arquivo_completo_novo = local_teste + vetor_aux2[pos]

	shutil.move(arquivo_completo_antigo, arquivo_completo_novo)