import torch
import torchvision.transforms  as transforms
import PIL.Image as Image
from pathlib import Path

class disasterclassifyer():
    def __init__(self):
        pass
    def initalize(self):

        self.classess = [
            "Cyclone",
            "Earthquake",
            "Flood",
            "Wildfire",
        ]
        mean =[0.4519, 0.4441, 0.4312]
        std=[0.2258, 0.2155, 0.2186]

        self.transform = ttrain_transforms = transforms.Compose([
            transforms.Resize((224,224)),
            transforms.ToTensor(),
            transforms.Normalize(torch.Tensor(mean),torch.Tensor(std))

        ])
        model_path = Path(__file__).with_name("Clamitydetect_ready.pth")
        self.model = torch.load(model_path, map_location="cpu", weights_only=False)
        self.model.eval()


    def classify(self,image_path):
            model = self.model
            image_transforms = self.transform
            classes = self.classess

            self.image_path = image_path

            model = model.eval()
            image = Image.open(self.image_path).convert("RGB")
            image = image_transforms(image).float()
            image = image.unsqueeze(0)
            with torch.no_grad():
                output = model(image)
            _ , predicted = torch.max(output.data, 1)

            return classes[predicted.item()]