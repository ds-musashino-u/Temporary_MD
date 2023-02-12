import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

# GPUの使用設定
device = 'mps'    
    
# データ前処理方法の定義
transform = transforms.Compose([
    transforms.ToTensor(),      # RGB数値をテンソルに変換
])

# データセットの用意
train_dataset = datasets.MNIST(root='', train=True, download=True, transform=transform)
val_dataset   = datasets.MNIST(root='', train=False, download=True, transform=transform)
train_loader  = DataLoader(train_dataset, batch_size=64, shuffle=True)
val_loader    = DataLoader(val_dataset, batch_size=64, shuffle=False)

# データセットの確認
data_iter = iter(train_loader)
imgs, labels = data_iter._next_data()

# 入力する画像のテンソルサイズ
data_iter = iter(train_loader)
imgs, labels = data_iter._next_data()
c, h, w = imgs[0].shape

# ネットワークの定義
# 2層(1*28*28:1024 - ReLU - 1024:512 - ReLU - 512:10)
class My_MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.classifer = nn.Sequential(
            nn.Linear(c * h * w, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )
    def forward(self,x):
        return self.classifer(x)

model = My_MLP()
model.to(device)

# 損失関数の設定（多クラス分類なので交差エントロピー誤差関数を使用）
criterion = nn.CrossEntropyLoss()

# 最適化関数の設定（モーメンタムSGDを使用）
optimizer = optim.Adam(model.parameters(),lr=0.001)

# Training：モデル学習
def model_training():
    model.train()
    train_loss = 0
    train_acc = 0

    for i, (images, labels) in enumerate(train_loader):
        images = images.view(-1,28*28)
        images = images.to(device)
        labels = labels.to(device)
      
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)

        train_loss += loss.item()
        pred = torch.argmax(outputs, dim=1)
        train_acc += (pred == labels).sum().item()

        loss.backward()
        optimizer.step()
        
    avg_train_loss = train_loss / len(train_loader.dataset)
    avg_train_acc = train_acc / len(train_loader.dataset)

    return avg_train_loss, avg_train_acc

# Validation：モデルのパラメータ評価
def model_val():
    model.eval()
    val_loss = 0
    val_acc = 0
    
    with torch.no_grad():
      for images, labels in val_loader:
          images = images.view(-1,28*28)
          images = images.to(device)
          labels = labels.to(device)

          outputs = model(images)
          loss = criterion(outputs, labels)
          
          val_loss += loss.item()
          pred = torch.argmax(outputs, dim=1)
          val_acc += (pred == labels).sum().item()

    avg_val_loss = val_loss / len(val_loader.dataset)
    avg_val_acc = val_acc / len(val_loader.dataset)

    return avg_val_loss, avg_val_acc

def main():
    num_epochs = 10
    train_loss_list = []
    train_acc_list = []
    val_loss_list = []
    val_acc_list = []

    for epoch in range(num_epochs):
        avg_train_loss = 0
        avg_train_acc = 0
        avg_val_loss = 0
        avg_val_acc = 0

        # モデル学習結果を受け取る
        avg_train_loss, avg_train_acc = model_training()

        # モデルのパラメータ評価結果を受け取る
        avg_val_loss, avg_val_acc = model_val()

        print ('Epoch [{}/{}], Loss: {loss:.4f}, val_loss: {val_loss:.4f}, val_acc: {val_acc:.4f}' 
                       .format(epoch+1, num_epochs, loss=avg_train_loss, val_loss=avg_val_loss, val_acc=avg_val_acc))
        train_loss_list.append(avg_train_loss)
        train_acc_list.append(avg_train_acc)
        val_loss_list.append(avg_val_loss)
        val_acc_list.append(avg_val_acc)
        
if __name__ == "__main__":
    main()