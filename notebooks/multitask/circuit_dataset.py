import torch.utils.data
import os
import cv2
import PIL.Image
import torch
import glob


class CircuitDataset(torch.utils.data.Dataset):
    def __init__(self, directory, num_timesteps, gamma=5e-3, transform=None):
        self.directory = directory
        self.image_paths = sorted(glob.glob(os.path.join(self.directory, '*.jpg')))
        self.num_timesteps = num_timesteps
        self.transform = transform
        self.gain = torch.exp(-3e-2*torch.linspace(0.0, num_timesteps, num_timesteps))
        
    def __len__(self):
        return len(self.image_paths) - self.num_timesteps
    
    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = PIL.Image.fromarray(image)
        width = image.width
        height = image.height
        
        if self.transform is not None:
            image = self.transform(image)
            
        target = torch.zeros(self.num_timesteps)
        for i in range(self.num_timesteps):
            path = os.path.splitext(os.path.basename(self.image_paths[idx + i]))[0]
            x = float(int(path.split('_')[1]) - 50) / 50.0
            target[i] = x
        
        return image, torch.sum(self.gain * torch.abs(target) / torch.sum(self.gain), dim=0, keepdim=True)