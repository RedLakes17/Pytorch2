#Carguemos un set de imagenes para trabajar con ellas

from torchvision.datasets import ImageFolder
from torchvision import transforms

#Define transformations para poder usar las imagenes
train_transforms=transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((128,128)),
])

dataset_train=ImageFolder(
    'data/clouds_train',
    transform=train_transforms,
)