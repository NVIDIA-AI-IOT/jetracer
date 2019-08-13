import torch
import os
import glob
import uuid
import PIL.Image
import torch.utils.data
import subprocess
import cv2
import numpy as np


class XYDataset(torch.utils.data.Dataset):
    
    def __init__(self, directory, transform=None, random_hflip=False):
        super(XYDataset, self).__init__()
        self.directory = directory
        self.transform = transform
        self.refresh()
        self.random_hflip = random_hflip
        
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, idx):
        
        image_path = self.image_paths[idx]
        
        x = int(image_path.split('_')[0])
        y = int(image_path.split('_')[1])
        
        image = cv2.imread(ann['image_path'], cv2.IMREAD_COLOR)
        image = PIL.Image.fromarray(image)
        width = image.width
        height = image.height
        
        if self.transform is not None:
            image = self.transform(image)
        
        x = 2.0 * (ann['x'] / width - 0.5) # -1 left, +1 right
        y = 2.0 * (ann['y'] / height - 0.5) # -1 top, +1 bottom
        
        if self.random_hflip and float(np.random.random(1)) > 0.5:
            image = torch.from_numpy(image.numpy()[..., ::-1].copy())
            x = -x
            
        return image, torch.Tensor([x, y])
    
    def refresh(self):
        self.image_paths = glob.glob(os.path.join(self.directory, '*.jpg'))
        
    def save_entry(self, image, x, y):
        filename = '%d_%d_%s.jpg' % (x, y, str(uuid.uuid1()))
        image_path = os.path.join(self.directory, filename)
        
        if not os.path.exists(self.directory):
            subprocess.call(['mkdir', '-p', self.directory])
            
        with open(image_path, 'wb') as f:
            cv2.imwrite(image_path, image)
            
        self.refresh()