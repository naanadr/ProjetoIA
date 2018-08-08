import matplotlib.pyplot as plt

acuracia_final = [0.63497, 0.64103, 0.63414, 0.62937]
taxa_aprendizado = [0.1, 0.2, 0.5, 1]

plt.figure(1)
plt.plot(taxa_aprendizado, acuracia_final, 'yo-')
plt.xticks(taxa_aprendizado)
plt.ylabel('Acuracia'), plt.xlabel('Taxa de aprendizado'), plt.title('Perceptron - Acuracia final')
plt.savefig('acuracia_total.png')

# -----------------------------------------------------------------------------------
acuracia_teste1 = [0.6168, 0.6181, 0.6471, 0.6539, 0.6349]
acuracia_teste2 = [0.6709, 0.6286, 0.6277, 0.6390, 0.6387]
acuracia_teste3 = [0.6580, 0.6329, 0.6320, 0.6326, 0.6150]
acuracia_teste4 = [0.6774, 0.6434, 0.5735, 0.6114, 0.6408]
folds = [0, 1, 2, 3, 4]

plt.figure(2)
plt.plot(acuracia_teste1, 'ro:')
plt.xticks(folds), plt.yticks(acuracia_teste1)
plt.xlabel('Pasta de teste'), plt.ylabel('Acuracia'), plt.title('100 eras e taxa de aprendizado 0.1')
plt.savefig('teste1.png')

plt.figure(3)
plt.plot(acuracia_teste2, 'ro:')
plt.xticks(folds), plt.yticks(acuracia_teste2)
plt.xlabel('Pasta de teste'), plt.ylabel('Acuracia'), plt.title('100 eras e taxa de aprendizado 0.2')
plt.savefig('teste2.png')

plt.figure(4)
plt.plot(acuracia_teste3, 'ro:')
plt.xticks(folds), plt.yticks(acuracia_teste3)
plt.xlabel('Pasta de teste'), plt.ylabel('Acuracia'), plt.title('100 eras e taxa de aprendizado 0.5')
plt.savefig('teste3.png')

plt.figure(5)
plt.plot(acuracia_teste4, 'ro:')
plt.xticks(folds), plt.yticks(acuracia_teste4)
plt.xlabel('Pasta de teste'), plt.ylabel('Acuracia'), plt.title('100 eras e taxa de aprendizado 1')
plt.savefig('teste4.png')
