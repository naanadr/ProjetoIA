# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

'''Informações para o relatorio:
as figuras tem dimensões diferentes que variam de 64-65 (h e w) ou 60-65....
- tamanho novo 80-80

gerar um vetor com as informações das imagens
serão 80 vetores, com 80 informações em cada um
'''

import cv2
import os
import imutils
from skimage.feature import hog
import numpy as np
import random

class Perceptron:
	# incializa o perceptron
	def __init__(self, epocas, taxa_aprendizagem):
		self.entradas = []            # entradas para teste
		self.saidas = []              # suas saidas esperadas para cada entrada
		self.epocas = epocas
		self.taxa_aprendizagem = taxa_aprendizagem
		self.pesos = []                         # vetor com os pesos que serão atribuidos a cada entrada
		self.total_entradas = 0     # quantidade total de entradas que serão testadas
		self.total_variaveis_entrada = 4225     # são 65 vetores com 65 dados em cada um, no caso, 65 * 65 = 4225
		self.arquivo = ""

	def preencher_vetor(self):
		# onde cada posição armazena um vetor com os pesos iniciais
		for i in range(4225):           # serão 4900 dados dentro de cada vetor
			# preencher o vetor que armazena os pesos
			self.pesos.append(np.random.random_sample())

	def treinar(self):
		# roda o algoritmo ate terminar as eras estabelecidas
		for i in range(self.epocas):
			erro = False
			# repetir o processo a quantidade total de entradas
			for j in range(self.total_entradas):
				if len(self.entradas[j]) == 4225:
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
			# se achar os melhores valores antes do fim das eras
			if not erro:
				print 'saiu pq não achou nenhum erro'
				break

	def testar(self):
		descritorControlador = Descritor(self.arquivo)

		amostras, resposta_esperada = descritorControlador.gerar_vetor()
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
		return 1 if valor >= 0 else 0

class Descritor:
	def __init__(self, arquivo):
		self.vetor_caracteristica = []
		self.saidas_esperadas = []
		self.arquivo = arquivo

	# gera o vetor de caracteristica
	def gerar_vetor(self):
		local = os.listdir(self.arquivo)
		random.shuffle(local)
		for im_file in local:
			im_path = self.arquivo + '/' + im_file
			im = cv2.imread(im_path, 0)

			# redimensiona a imagem
			im = imutils.resize(im, width=65, height=65)

			h, w = im.shape[:2]

			if h == 65 and w == 65:
				# converte a imagem em um vetor
				vetor_cara = np.asarray(im, dtype='uint8')

				# o resultador é um vetor de 80 posicoes, onde cada posição é um outro vetor com 80 valores
				# concatena todos os vetores em um vetor só
				vetor_aux = np.array(vetor_cara).ravel()

				# Realizar a normalização dos dados
				tam = len(vetor_aux)
				vetor_aux_2 = []
				for i in range(tam):
					val = vetor_aux[i] - min(vetor_aux)
					val2 = max(vetor_aux) - min(vetor_aux)
					if val2 == 0:
						vetor_aux_2.append(0)
					else:
						vetor_aux_2.append(val/float(val2))

				string_aux = im_file.split('.')[0]

				if not all([v == 0 for v in vetor_aux_2]) and not all([v == 1 for v in vetor_aux_2]):
					if 'nod' == string_aux:
						cont = 1
					elif 'nnod' == string_aux:
						cont = 0
					self.saidas_esperadas.append(cont)
					self.vetor_caracteristica.append(vetor_aux_2)
		return self.vetor_caracteristica, self.saidas_esperadas

# ---------------------------------------------------------------------------------------------------
# MAIN:

# Local com os arquivos:
string_path = "folds/"
accuracy_array = list()

# Posição do folder para teste:
for i in range(5):
	# Local do folder de teste:
	teste = string_path + str(i) + "fold"            #Separar para Teste
	print 'Teste sendo realizado no: ', teste

	# Instanciar a classe perceptron:
	perceptronControlador = Perceptron(100, 1)
	# Inicia os pesos com valores aleatorios, para o primeiro teste
	perceptronControlador.preencher_vetor()
	# Folder que serão utilizados para treinamento:
	for n in range(5):
		# Do folder 0 ate 4, ele treina com todas os folders, menos com o folder que é ele mesmo.
		if not n == i:
			# Diretorio com os arquivos de treinamento
			treino = string_path + str(n) + "fold"    #Treino da vez
			print 'treino: ', treino

			descritorTreinamento = Descritor(treino)

			print 'gerar vetor | retirar_informacoes...'
			# Separar os dados que compoem o vetor de caracteristica
			entradas, saidas = descritorTreinamento.gerar_vetor()

			print 'preencher variaveis...'
			# Insere os dados obtidos anteriormente:
			perceptronControlador.entradas = entradas
			perceptronControlador.total_entradas = len(entradas)
			#perceptronControlador.total_variaveis_entrada = len(entradas[0])
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
	accuracy = float(similar) / float(total)
	accuracy_array.append(accuracy)

	print 'acertados ', similar
	print 'total ', total
	print 'acuracia', accuracy
	print '\n'

soma = sum(accuracy_array)
result = soma / 5
print 'resultado final ', result