# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import numpy as np

class MLP:
    # na variavel camada, ele recebe a quantidade de camadas intermediárias do MLP
    def __init__(self, entradas, saidas, epocas, limiar, taxa_aprendizagem, camadas, neuronio_camada):
        self.entradas = entradas  # entradas para teste
        self.saidas = saidas  # suas saidas esperadas para cada entrada
        self.epocas = epocas
        self.limiar = limiar
        self.taxa_aprendizagem = taxa_aprendizagem
        self.pesos = []  # vetor com os pesos que serão atribuidos a cada entrada
        self.total_entradas = len(entradas)  # quantidade total de entradas que serão testadas
        self.total_variaveis_entrada = len(entradas[0])
        self.camadas = camadas
        self.pesos_camada = []
        self.neuronio_camada = neuronio_camada

    def treinar(self):
        # gerar pesos aleatorios
        for i in range(self.total_entradas):
            self.pesos.append(np.random.random_sample())

        # repete por num numero x+1 de repetições
        # se o MLP tiver 2 camadas, será necessários rodar 3 vezes, pra calcular o peso dos caminhos 3 vezes
        #for camada in range(self.camadas+1):