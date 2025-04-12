'''A veces los gradientes no crecen o crecen mucho conforme el backward avanza hacia atras, provocando problemas en las actializaciones de los parametros de las primeras capas
Vanishing gradients and Exploding gradients'''

#Para evitar esto podemos inicializar los pesos adecuadamente. Esto asegura que la varianza de las entradas sea igual a la de las salidas y que la varianza de los gradientes tambien sea estable
#Para ReLU podemos usar He/Kaiming initialization
import torch.nn.init as init
import torch.nn as nn

Layer1=nn.Linear(8,20)
init.kaiming_uniform_(Layer1.weight)


#Batch normalization es otra forma de afrontar la inestabilidad de los gradientes. Normaliza las salidas de las capas
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(9,16)
        self.bn1=nn.BatchNorm1d(16)
