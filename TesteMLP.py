# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

'''
    CÓDIGO PARA GERAR OS PESOS COM N NEURONIOS DE ENTRADA,
    PARA W CAMADAS INTERMEDIARIAS, ONDE CADA UMA POSSUE UMA QUANTIDADE
    X DE NEURONIOS. Para por fim, ir para um neuronio de saida.
'''

pesos_camada = []
# número de neuronios por camada intermediaria
neuronio_camada = [4, 4]
# número de neuronios na entrada
entradas = 2

vet_aux = []

neuronio_camada.insert(0, entradas)
# neuronio_camada = [2, 4, 4]
# len = 3

# repete qtd_camadas + 1 vez
for w in range(len(neuronio_camada)):
    # se for a primeira malha de conexões antes da 1 camada intermediaria
    if w == 0:
        vet_aux = []
        for i in range(entradas):
            pesos = []
            for j in range(neuronio_camada[w+1]):
                pesos.append(np.random.random_sample())
            vet_aux.append(pesos)
            #print 'vetor auxiliar ', vet_aux
        pesos_camada.append(vet_aux)
        #print 'pesos_camada ', pesos_camada, '\n'
    elif w == len(neuronio_camada)-1:
        vet_aux = []
        pesos = []
        for i in range(neuronio_camada[w]):
            pesos.append(np.random.random_sample())
        vet_aux.append(pesos)
        #print 'vetor auxiliar ', vet_aux
        pesos_camada.append(pesos)
        #print 'pesos_camada ', pesos_camada, '\n'
    else:
        vet_aux = []
        for j in range(neuronio_camada[w]):
            pesos = []
            for i in range(neuronio_camada[w+1]):
                pesos.append(np.random.random_sample())
            vet_aux.append(pesos)
            #print 'vetor auxiliar ', vet_aux
        pesos_camada.append(vet_aux)
        #print 'pesos_camada ', pesos_camada, '\n'


print '---------------------------------------------------------'
# len(pesos_camada) = 3
# referente a quantidade total de malhas de sinapses desse conjunto

# pesos referentes as ligações dos neuronios de entrada
print pesos_camada[0]
# pesos do primeiro neuronio de *entrada* para todos os neuronios da primeira sub camada
print pesos_camada[0][0]
# peso do primeiro neuornio de entrada para o primeiro neuornio da primeira sub camada
print pesos_camada[0][0][0]