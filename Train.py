 #i ran a simple mean and std code from chrome to get the values
#  PS C:\Users\ADITYA\Downloads\disaster image.v5i.folder> & C:\Users\ADITYA\AppData\Local\Programs\Python\Python312\python.exe "c:/Users/ADITYA/Downloads/disaster image.v5i.folder/Train.py"
#(tensor([0.4519, 0.4441, 0.4312]), tensor([0.2258, 0.2155, 0.2186]))
#PS C:\Users\ADITYA\Downloads\disaster image.v5i.folder> 

import os 
import time
import torch
import torchvision
import torchvision.transforms  as transforms

train_dataset_path = "./train/"
valid_dataset_path = "./valid/"

mean =[0.4519, 0.4441, 0.4312]
std=[0.2258, 0.2155, 0.2186]

train_transforms = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor(),
    transforms.Normalize(torch.Tensor(mean),torch.Tensor(std))

])
test_transforms = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(torch.Tensor(mean),torch.Tensor(std))
    
])
train_dataset = torchvision.datasets.ImageFolder(root= train_dataset_path,transform=train_transforms)

test_dataset = torchvision.datasets.ImageFolder(root= valid_dataset_path,transform=test_transforms)
train_class_to_idx = train_dataset.class_to_idx
test_dataset.samples = [
    (path, train_class_to_idx[os.path.basename(os.path.dirname(path))])
    for path, _ in test_dataset.samples
    if os.path.basename(os.path.dirname(path)) in train_class_to_idx
]
test_dataset.imgs = test_dataset.samples
test_dataset.targets = [target for _, target in test_dataset.samples]


train_loder = torch.utils.data.DataLoader(train_dataset,batch_size=32,shuffle=True)

test_loder = torch.utils.data.DataLoader(test_dataset,batch_size=32,shuffle=True)

def set_device():
    if torch.cuda.is_available():
        dev = "cuda"
    else:
        dev = "cpu"
    return torch.device(dev)

def save_checkpoint(model,epoch,optimizer,best_acc):
    state = {
        'epoch': epoch+1,
        'model':model.state_dict(),
        'best accuracy':best_acc,
        'optimizer': optimizer.state_dict(),
    }
    torch.save(state, 'Clamitydetect.pth.tar')
    torch.save(model, 'Clamitydetect_ready.pth')


def torch_nn(model, train_loader,test_loader,certiation,optimizer,n_epochs):
    device = set_device()
    best_acc = 0
    training_start_time = time.time()
    for epoch in range(n_epochs):
        epoch_start_time = time.time()
        print("Epoch %d/%d" % (epoch + 1, n_epochs))
        model.train()
        running_loss = 0.0
        running_correct = 0.0
        total = 0

        total_batches = len(train_loader)
        next_progress = 0.1
        for batch_index, data in enumerate(train_loader):
            images, lables = data
            images = images.to(device)
            lables = lables.to(device)
            total += lables.size(0)

            optimizer.zero_grad()

            outputs = model(images)

            _, predicted = torch.max(outputs.data,1)
            loss = certiation(outputs,lables)

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

            running_correct += (lables == predicted). sum().item()

            processed_batches = epoch * total_batches + batch_index + 1
            total_batches_to_process = n_epochs * total_batches
            elapsed_time = time.time() - training_start_time
            average_batch_time = elapsed_time / processed_batches
            remaining_batches = total_batches_to_process - processed_batches
            remaining_time = average_batch_time * remaining_batches
            iteration_speed = processed_batches / elapsed_time if elapsed_time > 0 else 0
            sample_speed = total / elapsed_time if elapsed_time > 0 else 0
            current_loss = running_loss / (batch_index + 1)
            current_acc = 100 * running_correct / total
            progress = (batch_index + 1) / total_batches
            if progress >= next_progress or batch_index + 1 == total_batches:
                print(
                    "  progress %.1f/1.0 | batch %d/%d | loss: %.4f | "
                    "accuracy: %.2f%% | speed: %.2f it/s (%.1f images/s) | "
                    "time remaining: %s"
                    % (
                        min(progress, 1.0),
                        batch_index + 1,
                        total_batches,
                        current_loss,
                        current_acc,
                        iteration_speed,
                        sample_speed,
                        time.strftime("%H:%M:%S", time.gmtime(remaining_time)),
                    ),
                    flush=True,
                )
                next_progress += 0.1
        epoch_loss = running_loss/len(train_loader)
        epoch_acc = 100*running_correct/total
        test_data_acc = eveauate_model_on_test_set(model,test_loader)
        if test_data_acc > best_acc:
            best_acc = test_data_acc
            save_checkpoint(model,epoch,optimizer,best_acc)

        epoch_time = time.time() - epoch_start_time
        elapsed_time = time.time() - training_start_time
        average_epoch_time = elapsed_time / (epoch + 1)
        remaining_time = average_epoch_time * (n_epochs - epoch - 1)
        print(
            "  loss: %.4f | train accuracy: %.2f%% | validation accuracy: %.2f%% | "
            "epoch time: %s | time remaining: %s | best accuracy: %.2f%%"
            % (
                epoch_loss,
                epoch_acc,
                test_data_acc,
                time.strftime("%H:%M:%S", time.gmtime(epoch_time)),
                time.strftime("%H:%M:%S", time.gmtime(remaining_time)),
                best_acc,
            )
        )
    print("Finished")
    return model




def eveauate_model_on_test_set(model,test_loader):
    model.eval()
    predict_correctly_on_epoch = 0
    total = 0
    device = set_device()
    with torch.no_grad():
        for data in test_loader:
            images, lables = data
            images = images.to(device)
            lables = lables.to(device)
            total += lables.size(0)
            outputs = model(images)
            
            _, predicted = torch.max(outputs.data,1)

            predict_correctly_on_epoch += (predicted == lables).sum().item()
    epoch_acc = 100.0 * predict_correctly_on_epoch / total
    print("         - Testing dataset. Got %d out of %d images correctly (%.3f%%)" % (predict_correctly_on_epoch,total,epoch_acc))
    return epoch_acc

            



    

import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
reanetmodel = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
num_ftrs = reanetmodel.fc.in_features
number_of_classes = len(train_dataset.classes)
reanetmodel.fc = nn.Linear(num_ftrs,number_of_classes)

device = set_device()
reanetmodel = reanetmodel.to(device)
loss_fn = nn.CrossEntropyLoss()

optimizer = optim.SGD(reanetmodel.parameters(), lr=0.01, momentum=0.9, weight_decay=0.0003)


torch_nn(reanetmodel, train_loder,test_loder,loss_fn,optimizer,n_epochs=15)



