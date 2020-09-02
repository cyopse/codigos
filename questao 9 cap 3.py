import random
import math

def high(array):
    print('array criado: ', end = '')
    print (array)
    media = sum(array)/len(array)
    power = []
    for num in array:
        power.append(num**2)
    desvio = (sum(power)/len(array)) - media**2
    array.sort()
    print('array ordenado: ', end = '')
    print(array)
    moda = float()
    ccounter = 0
    acounter = 0
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            ccounter += 1
            if ccounter > acounter:
               acounter = ccounter
               moda = array[i]
        else:
            ccounter = 0
    mediana = array[math.floor(len(array)/2)]
    print(' media: {} \n desvio: {} \n moda: {} \n mediana: {}'.format(media, desvio, moda, mediana))
   
lista = []
   
for i in range(11):
    lista.append(random.randint(10,20))

high(lista)