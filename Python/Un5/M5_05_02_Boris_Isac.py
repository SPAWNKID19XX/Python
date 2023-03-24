import numpy as np
dolar = np.random.randint(1, 1000 + 1, 100)
print('Dolar: \n',dolar)
print('Euros:')
np.set_printoptions(precision=2)
euro = 0.874413 * dolar
print(euro)



