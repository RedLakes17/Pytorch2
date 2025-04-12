from torch.utils.data import Dataset
import pandas as pd

#Creamos la clase
class WaterDataset(Dataset):
    def __init__(self, csv_path):
        super().__init__()
        df=pd.read_csv(csv_path)
        self.data=df.to_numpy()
    def __len__(self):
        return self.data.shape[0]
    def __getitem__(self, idx):
        features=self.data[idx,:-1]
        label=self.data[idx,-1]
        return features, label


#Creamos un oobjeto de la clase con un archivo
dataset_train= WaterDataset('water_train.csv')

#Luego, pasamos el dataset al dataloader
from torch.utils.data import DataLoader
dataloader_train=DataLoader(dataset_train, batch_size=2, shuffle=True)


#Si usamos classes para definir modelos tenemos mas flexibilidad
import torch.nn as nn

class Net(nn.Module()):
    def __init__(self): #Constructor de la clase. Se ejecuta cada vez que se agrega un objeto
        super().__init__() #Llama al constructor de la clase padre, inicializando correctamente nn.Module
        self.fc1 = nn.Linear(9,16)
        self.fc2 = nn.Linear(16,8)
        self.fc3 = nn.Linear(8,1)
    def forward(self, x):
        x=nn.functional.relu(self.fc1(x))
        x=nn.functional.relu(self.fc2(x))
        x=nn.functional.sigmoid(self.fc3(x))
        return x
    
net=Net()




