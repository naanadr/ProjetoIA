# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import numpy as np

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


'''
acho
'''

# Perceptron com apenas uma camada
class Perceptron:
    # TODO define um valor para o limiar, epoca e a taxa de aprendizagem?
    # TODO estou presumindo que o vetor saida contem apenas a saida deseja para cada amostra, estou certa? Precisa fazer uma função para isso?
    # incializa o perceptron
    def __init__(self, entradas, saidas, epocas, limiar, taxa_aprendizagem):
        self.entradas = entradas                # entradas para teste
        self.saidas = saidas                    # suas saidas esperadas
        self.epocas = epocas
        self.limiar = limiar
        self.taxa_aprendizagem = taxa_aprendizagem
        self.pesos = []                         # vetor com os pesos que serão atribuidos a cada entrada
        self.total_entradas = len(entradas)     # quantidade total de entradas que serão testadas
        self.total_variaveis_entrada = len(entradas[0])

    def treinar(self):
        for i in range(self.total_entradas):                                            # um vetor de vetores, onde cada posição armazena um vetor com os pesos referentes a cada variavel da entrada
            self.pesos.append(np.random.random_sample(self.total_variaveis_entrada))    # preencher o vetor que armazena os pesos

        # TODO terminar de rodar quando acabar as eras? ou quando nao estiver mais erros? ou os dois?
        for i in range(self.epocas):                        # roda o algoritmo ate terminar as eras estabelecidas
            #erro = False                                    # erro inicialmente falso

            for j in range(self.total_entradas):            # repetir o processo a quantidade total de entradas
                somatorio = 0

                for posicao in range(self.total_variaveis_entrada):              # somar os pesos com as entradas
                    somatorio += self.pesos[j][posicao] * self.entradas[j][posicao]

                # função de ativação
                if somatorio >= self.limiar: saida = 1
                else: saida = 0

                if saida != self.saidas[j]:
                    #erro = True
                    erro_auxiliar = self.saidas[j] - saida

                    for posicao in range(self.total_variaveis_entrada):             # corrigir o peso agora para cada entrada dessa rodada
                        self.pesos[j][posicao] = self.pesos[j][posicao] + (self.taxa_aprendizagem * erro_auxiliar * self.entradas[j][posicao])

    #def executar(self):