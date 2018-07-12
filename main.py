# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

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