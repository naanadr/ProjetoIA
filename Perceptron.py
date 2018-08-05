# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import cv2
import os
import imutils
from skimage.feature import hog
import numpy as np
import random
import copy

'''
Descrição do algoritmo:
	1 - entradas
	2 - peso de desvio
	3 - função de entrada
	4 - função de ativação
	5 - função de saida
'''

'''
Função de ativação:
	1 - Soma ponderada das entradas (entrada*peso)
	2 - Colocar a soma na função de ativação
	
	A função pode ser do tipo:
		threshold:
		*se* g(somas) >= ao treshold *é* 1
		*se* g(somas) < treshold *é* 0
		
		sigmoid logistica
		
		tangente hiperbólica
		
Depois aplicar o resultado obtido com o resultado esperado, 
se for diferente utilizar uma função de correção de erro

Erro:
	1 - erro (e) = resultadoObtido - resultadoEsperado
	
	2 - função de custo (c) = 1/(2*(soma de e^2(t)))
	
	3 - função de aprendizado(W) = n(função de aprendizado) * e * valor da entrada
	
	4 - novo peso =  peso + resultado de W
'''

'''
Variáveis necessárias:
	1 - entradas
	2 - pesos
	3 - limiar
	4 - função de aprendizado
'''

# Perceptron com apenas uma camada
class Perceptron:
	# incializa o perceptron
	def __init__(self, epocas, taxa_aprendizagem):
		self.entradas = []            # entradas para teste
		self.saidas = []              # suas saidas esperadas para cada entrada
		self.epocas = epocas
		self.taxa_aprendizagem = taxa_aprendizagem
		self.pesos = []                         # vetor com os pesos que serão atribuidos a cada entrada
		self.total_entradas = 0     # quantidade total de entradas que serão testadas
		self.total_variaveis_entrada = 0
		self.arquivo = ""

	def preencher_vetor(self):
		# onde cada posição armazena um vetor com os pesos iniciais
		for i in range(648):
			# preencher o vetor que armazena os pesos
			self.pesos.append(np.random.random_sample())

	def treinar(self):
		# roda o algoritmo ate terminar as eras estabelecidas
		for i in range(self.epocas):
			erro = False
			# repetir o processo a quantidade total de entradas
			for j in range(self.total_entradas):
				if len(self.entradas[j]) == 648:
					somatorio = 0
					# somar os pesos com as variaveis da entrada
					for posicao in range(self.total_variaveis_entrada):
						somatorio += self.pesos[posicao] * self.entradas[j][posicao]

					# função de ativação
					saida = self.ativacao(somatorio)

					if saida != self.saidas[j]:
						erro = True
						erro_auxiliar = self.saidas[j] - saida

						# corrigir o peso agora para cada entrada dessa rodada
						for posicao in range(self.total_variaveis_entrada):
							self.pesos[posicao] = self.pesos[posicao] + \
												  (self.taxa_aprendizagem * erro_auxiliar * self.entradas[j][posicao])
				else:
					print 'não possui 648 caracteristicas'
			# se achar os melhores valores antes do fim das eras
			if not erro:
				print 'não encontrou mais erro'
				break

	def testar(self):
		resposta_esperada = []
		amostras = []
		local = os.listdir(self.arquivo)
		cont = 0

		hogControlador = hog_gerador()

		for im_file in local:
			vetor_caracteristica_aux = []

			im_path = self.arquivo + im_file

			im = cv2.imread(im_path)

			fd, hog_image = hogControlador.hog_utilizar(im)

			for i in range(len(fd)):
				teste = float(fd[i])
				vetor_caracteristica_aux.append(teste)

			string_aux = im_file.split('.')[0]
			if 'nodule' == string_aux:
				cont = 1
			elif 'nannodule' == string_aux:
				cont = 0

			resposta_esperada.append(cont)
			amostras.append(vetor_caracteristica_aux)

		resposta = []
		for amostra in amostras:
			# utiliza o vetor de pesos que foi ajustado na fase de treinamento
			u = 0
			for i in range(self.total_variaveis_entrada):
				u += self.pesos[i] * amostra[i]

			# calcula a saída da rede
			y = self.ativacao(u)

			resposta.append(y)

		return resposta, resposta_esperada

	# função de ativação do tipo bipolar (bipolar pq so tem dois valores de saida)
	# +1 ativo e 0 inativo, com 0 como limiar
	def ativacao(self, valor):
		#return 1 if valor >= 0 else -1
		return 1 if valor >= 0 else 0

class hog_gerador:
	def __init__(self, arquivos_treino):
		self.vetor_caracteristica = []
		self.saidas_esperadas = []
		self.arquivos = arquivos_treino + '/'

	def hog_utilizar(self, im):
		resized_image = imutils.resize(im, width=80, height=80)

		fd, hog_image = hog(resized_image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(3, 3),
		                    visualize=True, feature_vector=True)

		print 'aqui ', fd

		return fd, hog_image

	def gerar_vetor(self):
		local = os.listdir(self.arquivos)
		cont = 0

		for im_file in local:
			vetor_caracteristica_aux = []

			im_path = self.arquivos + im_file

			im = cv2.imread(im_path)

			fd, hog_image = self.hog_utilizar(im)

			for i in range(len(fd)):
				teste = float(fd[i])
				vetor_caracteristica_aux.append(teste)

			string_aux = im_file.split('.')[0]
			if 'nodule' == string_aux:
				cont = 1
			elif 'nannodule' == string_aux:
				cont = 0
			vetor_caracteristica_aux.append(cont)

			self.vetor_caracteristica.append(vetor_caracteristica_aux)

		random.shuffle(self.vetor_caracteristica)

	def retirar_informacoes(self):
		entradas = []
		saidas = []

		for vetor in self.vetor_caracteristica:
			# não utilizar os vetores de caracteristica que só são compostos por 0's
			if vetor[0] != 0:
				aux = len(vetor) - 1
				entradas.append(vetor[0:aux])
				saidas.append(vetor[len(vetor)-1])

		return entradas, saidas

# ---------------------------------------------------------------------------------------------------
# MAIN:

# Local com os arquivos:
string_path = "5_fold/"
accuracy_array = list()

# Posição do folder para teste:
for i in range(5):
	# Local do folder de teste:
	teste = string_path + str(i) + "fold"            #Separar para Teste
	print 'Teste sendo realizado no: ', teste

	# Instanciar a classe perceptron:
	perceptronControlador = Perceptron(100, 0.1)
	# Inicia os pesos com valores aleatorios, para o primeiro teste
	perceptronControlador.preencher_vetor()
	# Folder que serão utilizados para treinamento:
	for n in range(5):
		# Do folder 0 ate 4, ele treina com todas os folders, menos com o folder que é ele mesmo.
		if not n == i:
			# Diretorio com os arquivos de treinamento
			treino = string_path + str(n) + "fold"    #Treino da vez
			print 'treino: ', treino

			# Instanciar a classe do hog
			hogControlador = hog_gerador(treino)
			print 'gerar vetor...'
			# Gerar o vetor de caracteristica:
			hogControlador.gerar_vetor()

			entradas = []
			saidas = []
			print 'retirar_informacoes...'
			# Separar os dados que compoem o vetor de caracteristica
			entradas, saidas = hogControlador.retirar_informacoes()
			# Insere os dados obtidos anteriormente:
			perceptronControlador.entradas = entradas
			perceptronControlador.total_entradas = len(entradas)
			perceptronControlador.total_variaveis_entrada = len(entradas[0])
			perceptronControlador.saidas = saidas

			print 'treinar...'
			# Inicia o processo de treinamento:
			perceptronControlador.treinar()

	print 'testar...'
	# Passa o diretorio que está os dados de teste:
	perceptronControlador.arquivo = teste
	resposta_obtida, resposta_esperada = perceptronControlador.testar()

	similar = 0
	print 'somando...'
	for i in range(len(resposta_obtida)):
		if resposta_obtida[i] == resposta_esperada[i]: similar += 1
	total = len(resposta_obtida)
	accuracy = float(similar)/ float(total)
	accuracy_array.append(accuracy)

	print 'acertados ', similar
	print 'total ', total
	print 'acuracia', accuracy
	print '\n'

soma = sum(accuracy_array)
result = soma / 5
print 'resultado final ', result
'''for i in accuracy_array:
	print i
	soma = soma + i'''